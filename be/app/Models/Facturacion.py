

from app import app, db
from functools import wraps
from datetime import datetime

from app.Models.Dominios import DominiosTipos

with app.app_context():
    db.reflect()
    
class Facturacion(db.Model):
    __table__ = db.metadata.tables["facturacion"]
     
    def __repr__(self):
        return '<Facturacion %r>' % self.id
    def toDict(self):
        return{
            "id": self.id,
            "id_acceso": self.id_acceso,
            "id_acceso_creacion": self.id_acceso_creacion,
            "id_facturacion_credito": self.id_facturacion_credito,
            "id_ubicacion": self.id_ubicacion,
            "forma_pago": self.forma_pago,
            "monto": self.monto,
            "num_recibo": self.num_recibo,
            "num_cheque": self.num_cheque,
            "num_transaccion": self.num_transaccion,
            "nombre": self.nombre,
            "email": self.email,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "estado": self.estado,
            "ccnumero": self.ccnumero,
            "authcode": self.authcode,
            "nota_credito": self.nota_credito,
            "fecha_pago": self.fecha_pago,
            "fecha_creacion": self.fecha_creacion,
        }

class FacturacionCreditos(db.Model):
    __table__ = db.metadata.tables["facturacion_creditos"]
        

    def __repr__(self):
            return '<FacturacionCreditos %r>' % self.id
    
    def toDict(self):
        return{
            "id": self.id,
            "id_acceso": self.id_acceso,
            "id_facturacion": self.id_facturacion,
            "id_facturacion_forma_pago": self.id_facturacion_forma_pago,
            "monto": self.monto,
            "saldo": self.saldo,
            "referencia": self.referencia,
            "tipo": self.tipo,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,
        }
        

class FacturacionServicios(db.Model):
    __table__ = db.metadata.tables["facturacion_servicios"]
        
    costos_details = db.relationship("FacturacionCostos", backref="FacturacionServicios")
  
    def __repr__(self):
            return '<FacturacionServicios %r>' % self.id
    
    def toDict(self):
        return{
            "id": self.id,
            "id_dominio_tipo": self.id_dominio_tipo,
            "tipo": self.tipo,
            "nombre": self.nombre,
            "num_annos": self.num_annos,
            "costos_details": [r.toDict() for r in self.costos_details],
        }

class FacturacionCostos(db.Model):
    
    __table__ = db.metadata.tables["facturacion_costos"]
     
     
    def __repr__(self):
        return '<FacturacionCostos %r>' % self.id
    
    def toDict(self):
        return{
            "id": self.id,
            "id_facturacion_servicio": self.id_facturacion_servicio,
            "tipo": self.tipo,
            "costo": self.costo,
            "descuento": self.descuento,
            
        }


