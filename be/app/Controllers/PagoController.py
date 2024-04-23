import os


from . import ControllerObject

from flask import render_template
from app import *
import requests
import json
import random
import string

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from app.Models.Facturacion import Facturacion
from app.Models.Ubicaciones import PaisesUbicaciones

from app.Models.Dominios import (
    Dominios,
    DominiosTipos,
    DominiosDns,
    DominiosDnsIP,
)

from app.modules.payment.gwapi import gwapi
from flask_mail import Message


def PagoCredito(data):
    ret = ControllerObject()
    dominiosFactura = []
    costoTotal = 0

    try:
        iv = os.getenv("IV")

        userInfo = data.get("data")
        userInfo = b64decode(userInfo)
        salt = b64decode(os.getenv("ENCRYPT_SALT"))

        cipher = AES.new(salt, AES.MODE_CBC, iv.encode("utf-8"))
        userInfo = cipher.decrypt(userInfo)
        userInfo = unpad(userInfo, 16).decode("utf-8")
        userInfo = json.loads(userInfo)

        billing = userInfo.get("billing")
        order = userInfo.get("order")
        datos = userInfo.get("datos")
        dominios = userInfo.get("dominios")
        
        ubicacion = PaisesUbicaciones.query.filter(billing.get('country')==PaisesUbicaciones.id)\
                                            .with_entities(PaisesUbicaciones.nombre).scalar()
        userdata = {
            "nombre": billing.get("firstname"),
            "apellido": billing.get("lastname"),
            "empresa": billing.get("company"),
            "estado": billing.get("state"),
            "ciudad": billing.get("city"),
            "forma_pago": 'Tarjeta de credito',
            "email": billing.get("email"),
            "telefono": billing.get("phone"),
        }
        
        userdata['id_ubicacion'] = ubicacion

        nombre_completo = f'{billing.get("firstname")} {billing.get("lastname")}' 
        tiempo = datetime.now() - timedelta(hours=6)
        
        factura = Facturacion(
                id_acceso=billing.get("id_acceso"),
                id_acceso_creacion=billing.get("id_acceso"),
                forma_pago='tarjeta_credito',
                monto=datos.get("amount"),
                nombre=nombre_completo,
                fecha_pago=tiempo,
                fecha_creacion=tiempo,
            )
        
        db.session.add(factura)
        db.session.flush()
        
        gw = gwapi()
        gw.setLogin(security_key=os.getenv("MERCHANTKEY"))

        gw.setBilling(
            firstname=billing.get("firstname"),
            lastname=billing.get("lastname"),
            email=billing.get("email"),
            company=billing.get("company"),
            address1=billing.get("address1"),
            address2=billing.get("address2"),
            country=ubicacion,
            state=billing.get("state"),
            city=billing.get("city"),
            phone=billing.get("phone"),
        )
        
        gw.setOrder(
            orderid=factura.id,
            orderdescription=order.get("orderdescription"),
            ipaddress=order.get("ipaddress"),
        )

        r = gw.doSale(
            amount=datos.get("amount"),
            ccnumber=datos.get("ccnumber"),
            ccexp=datos.get("ccexp"),
            cvv=datos.get("cvv"),
        )

        if int(gw.responses["response"]) == 1:
            
            id_acceso = billing.get("id_acceso")
            str_ccnumber = str(datos.get("ccnumber"))
            tiempo = datetime.now() - timedelta(hours=6)
            masked_ccnumber = str_ccnumber[:4] + 'X' * 8 + str_ccnumber[12:]
            num_recibo = f"{generate_random_string(6)}-{id_acceso:06d}-{generate_random_string(6)}"
            num_transaccion = gw.responses['transactionid']
            authcode = gw.responses['authcode']

            factura_mod = Facturacion.query.get(factura.id)
            factura_mod.id_ubicacion=billing.get('country'),
            factura_mod.num_recibo=num_recibo,
            factura_mod.num_transaccion=num_transaccion,
            factura_mod.email=billing.get("email"),
            factura_mod.direccion=billing.get("address1"),
            factura_mod.ciudad=billing.get("city"),
            factura_mod.estado=billing.get("state"),
            factura_mod.ccnumero=masked_ccnumber,
            factura_mod.authcode=authcode,
        
            for e in dominios:
                
                subtotal = (e['price'] * e['years']) - e['discount']
                dominiosFactura.append({
                    "price": e['price'],
                    "discount": e['discount'],
                    "years": e['years'],
                    "type": e['type'],
                    "domain": e['domain'],
                    "subtotal": subtotal,
                })
                costoTotal += subtotal
                
                tiempo = datetime.now() - timedelta(hours=6)
                tipoDominio = e["domain"].split(".", 1)[-1]
                # guardar dominio
                tipodominioid = (
                    db.session.query(DominiosTipos)
                    .filter_by(nombre=f".{tipoDominio}")
                    .with_entities(DominiosTipos.id)
                    .scalar()
                )

                crear_dominio = Dominios(
                    id_dominio_tipo=tipodominioid,
                    id_dominio_estado=1,
                    id_acceso=billing.get("id_acceso"),
                    nombre=e["domain"],
                    cant_annos=e["years"],
                    fecha_solicitud=tiempo,
                    fecha_creacion=tiempo,
                    fecha_actualizacion=tiempo,
                )

                db.session.add(crear_dominio)
                db.session.flush()

                dominioid = crear_dominio.id

                for dns in e["ipServidoresDNS"]:

                    dominios_dns = DominiosDns(
                        id_dominio=dominioid,
                        nombre=dns["nombre"],
                        fecha_creacion=tiempo,
                    )
                    db.session.add(dominios_dns)
                    db.session.flush()

                    if dns.get('ipDNS') in dns:
                    
                        dominios_dns_ip = DominiosDnsIP(
                            id_dominio_dns=dominios_dns.id,
                            ip_servidor=dns["ipDNS"],
                            fecha_creacion=tiempo,
                        )
                        db.session.add(dominios_dns_ip)
                        db.session.flush()


            db.session.commit()
            
            num_factura = f'{factura.id:07d}'
            msg = Message()
            msg.subject = f'Factura - {num_factura}'
            msg.recipients = [billing.get("email")]
            msg.html = render_template(
                "correos/factura.html",
                user=userdata,
                dominiosFactura=dominiosFactura,
                costoTotal=costoTotal,
                num_factura=num_factura,
                date=tiempo.date(),
            )
            
            mail.send(msg)
            
            ret.payload = gw.responses
            ret.mensaje = "Se realizo la consulta exitosamente"
            ret.status = 200
            return ret

        elif int(gw.responses["response"]) == 2:

            db.session.rollback()
            ret.payload = gw.responses
            ret.mensaje = "la tarjeta ha sido reclinada"
            ret.status = 400
            return ret

        elif int(gw.responses["response"]) == 3:
            
            db.session.rollback()
            ret.payload = gw.responses
            ret.mensaje = f"Error en la transaccion"
            ret.status = 400
            return ret
        
            
    except (Exception) as err:
        db.session.rollback()
        print(err)
        ret.mensaje = f"No se pudo realizar la consulta. error: {err}"
        ret.status = 400
        return ret



def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def getOrder():
    orderId = db.session.query(Facturacion).order_by(Facturacion.id.desc()).first()
    orderId = orderId.toDict()
    orderId = orderId["id"] + 1
    return orderId


def getPrice(domain):
    ret = ControllerObject()
    try:

        aux = domain.split(".")
        if len(aux) <= 2:
            price = 100
        else:
            price = 25

        ret.payload = price

    except (Exception) as err:
        ret.mensaje = f"No se pudo realizar la consulta. error: {err}"
        ret.status = 400
        
    return ret




def PruebaEndpoint():
    ret = ControllerObject()
    
    ret.mensaje = "Se realizo la consulta exitosamente"
    ret.status = 200
    return ret
