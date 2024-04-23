import os
from flask import request, render_template
from app import app
from sqlalchemy.exc import IntegrityError, DataError, NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

import json
import base64
from datetime import datetime, timedelta

from app.Models.Users import User, Role, Permisos, db

from app.Models.UsersNic import UsuariosExternos, AccesoUsuarios

from werkzeug.security import check_password_hash

from app.modules.users.funciones import security

from . import ControllerObject

from flask_mail import Message

from app import *


def GetAllUsers():
    ret = ControllerObject()

    try:
        ret.payload = [usuario.toDict() for usuario in UsuariosExternos.query]
        ret.mensaje = 'Se realizo la consulta exitosamente'
        ret.status = 200

    except (Exception) as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret
    
def LoginUser(userLogin):
    
    ret = ControllerObject()
    emailLogin = userLogin['email']
    passwordLogin = base64.b64decode(userLogin['password']).decode('utf-8')
    
    try:
        
        existeUsuario = AccesoUsuarios.query.filter_by(email=emailLogin).first()
        
        if not existeUsuario or not check_password_hash(existeUsuario.contrasena, passwordLogin):
            ret.mensaje = 'Credenciales incorrectos'
            ret.status = 400
          
            return ret
        
        infoUsuario = UsuariosExternos.query.filter_by(id_acceso=existeUsuario.id).first()
        infoUsuario = infoUsuario.toDict()
        infoUsuario['email'] = userLogin['email']
        ret.payload = infoUsuario
        ret.mensaje = 'inicio de sesion exitoso'
        ret.status = 200
    
    except (Exception) as err:
        ret.mensaje = f"No se pudo realizar la consulta. error: {err}"
        ret.status = 400

    return ret


def RegisterUser(user):

    ret = ControllerObject()
    
    existeCorreo = db.session.query(AccesoUsuarios.id).filter_by(email=user['correo']).first() is not None

    try:

        if not existeCorreo:
            username = user['correo'].split('@')
            username = username[0]
            username = ''.join(letter for letter in username if letter.isalnum())
            hashPassword = generate_password_hash(user['password'])

            datetime_now = datetime.utcnow()
            offset = timedelta(hours=-5)
            fechaCreacion = datetime_now+offset


            acceso = AccesoUsuarios(
                usuario = username,
                email = user['correo'],
                contrasena = hashPassword,
                fecha_creacion = fechaCreacion
            )
        
            db.session.add(acceso)
            db.session.flush()
            
            usuarioExterno = UsuariosExternos(
                id_acceso = acceso.id,
                id_tipo_cliente = 1,
                id_ubicacion = user['ubicacion_id'],
                nombre = user['nombre'],
                apellido = user['apellido'],
                identificacion = user['identificacion'],
                telefono = user['telefono'],
                empresa = user['empresa'],
                cargo = user['cargo'],
                direccion1 = user['direccion1'],
                direccion2 = user['direccion2'],
                estado = user['estado'],
                ciudad = user['ciudad'],
                fecha_creacion = fechaCreacion,
                fecha_actualizacion = fechaCreacion,
            )
            
            db.session.add(usuarioExterno)
            db.session.commit()
        
        
            ret.mensaje = 'Registrado exitosamente'
            ret.status = 200
            
        else:
            ret.mensaje = f"El correo { user['correo'] } ya esta en uso"
            ret.status = 400

    except (Exception) as err:
            ret.mensaje = "No se pudo realizar la consulta."
            ret.status = 400

    return ret

def SendMailRecoverPassword(user):
    ret = ControllerObject()
    
    try:
        # Codigo que utiliza la informacion 
        userInfo = AccesoUsuarios.query.filter_by(email=user['email']).first()
        
        if userInfo is not None:

            token = userInfo.get_reset_token()

            msg = Message()
            msg.subject = 'Recuperar contraseña Westec  Panamá'
            msg.recipients = [user['email']]
            msg.html = render_template(
                "correos/reset_password.html",
                user=user,
                token=token,
                domain=os.getenv("SERVER"),
            )
        
            mail.send(msg)

            ret.mensaje = 'Si el email existe se envio un correo'
            ret.status = 200

        else:
            ret.mensaje = 'Si el email existe se envio un correo'
            ret.status = 200

    except (Exception) as err:
        ret.mensaje = f"{err} No se pudo realizar la consulta."
        ret.status = 400
    
    return ret

def ResetPassword(user):
    ret = ControllerObject()

    try:
        userInfo = AccesoUsuarios.verify_reset_token(user['token'])
        
        if userInfo is None:
            ret.mensaje = 'Token invalido o expirado'
            ret.status = 400
            return ret
        
        userInfo.contrasena = generate_password_hash(user['password'])
        db.session.commit()
        
        msg = Message()
        msg.subject = 'Contraseña cambiada Westec  Panamá'
        msg.recipients = [userInfo.email]
        msg.html = render_template("correos/changed_password.html")
        
        mail.send(msg)

        ret.mensaje = 'Se cambio la contraseña exitosamente'
        ret.status = 200

    except (Exception) as err:
        ret.mensaje = f"{err} No se pudo realizar la consulta."
        ret.status = 400
    
    return ret

def manage_usuarios(uid):
    ret = ControllerObject()

    try:
        if request.method == 'GET':
            usuario = User.query.filter_by(id=uid).first()

            if usuario:
                ret.payload = [User.toDict(usuario)]
            else:
                ret.mensaje = "El rol no fue encontrado"
                ret.status = 404
            
        elif request.method == 'POST':
           # valid_perms = getValidPermissions(request.json["role_permissions"])
            usuario = User.query.get(uid)
        
            if usuario:
                data = request.get_json()
                usuario.email = data['email']
            #    if request.json.get('password'):
            #        usuario.password = generate_password_hash(data['password']) 
                usuario.nombre = data['nombre']
                usuario.apellido = data['apellido']
                usuario.active = data['active']
                usuario.grupo_id = data['grupo_id']
                usuario.roles = []
                
                for r in data['roles']:
                    security.datastore.add_role_to_user(usuario, r)
                    db.session.commit()
                
                db.session.commit()
                ret.mensaje = "El usuario fue modificado exitosamente."
            
            else:
                usuario = User(
                    email = request.json["email"],
                #    password = generate_password_hash(request.json['password']),
                    nombre = request.json["nombre"],
                    apellido = request.json["apellido"],
                    active = request.json['active'],
                    grupo_id = request.json['grupo_id'],
                )

                for r in request.json['roles']:
                    security.datastore.add_role_to_user(usuario, r)
                    db.session.commit()
                
                db.session.add(usuario)
                db.session.commit()
                
                ret.mensaje = "Usuario creado exitosamente."
          
        elif request.method == 'DELETE':
            if int(uid) == 1:
                ret.mensaje = "No se puede eliminar el usuario maestro."
                ret.status = 400
            
            else:
                usuario = User.query.get(uid)

                if usuario:
                    db.session.delete(usuario)
                    db.session.commit()
                    ret.mensaje = "Usuario eliminado"
                
                else:
                    ret.mensaje = "No se encontró el usuario solicitado"
                    ret.status = 404
    
    except (Exception) as err:
        ret.mensaje = "No se puede completar la solicitud."
        ret.status = 400
    
    return ret


'''
def correo_notificacion(data):
    msg = Message()
    msg.subject = "Modificación de Contraseña"
    msg.sender = '"Cárnet UTP" <bolsadetrabajo@utp.ac.pa>'
    msg.recipients = [user.email]
    msg.html = render_template("correos/changed_password.html", user=user)

    mail.send(msg)

'''


def change_pass(uid):
    ret = ControllerObject()
    # ip_addr = request.remote_addr
    # print("Imprimiendo")
    # print(ip_addr)
    if request.method == 'POST':
        usuario = User.query.get(uid)
        if usuario:
            if request.json.get('original'):
                if check_password_hash(usuario.password, request.json.get('original')):
                    data = request.get_json()
                    usuario.password = generate_password_hash(data['password']) 
                    db.session.commit()
                    ret.mensaje = "La contraseña fue modificada exitosamente."
                    ret.status = 200
                else:
                    ret.mensaje = "La contraseña original no concuerda."
                    ret.status = 401
    return ret