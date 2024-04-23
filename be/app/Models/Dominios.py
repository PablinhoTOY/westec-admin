

from app import app, db
from functools import wraps
import uuid
from datetime import datetime



with app.app_context():
    db.reflect()


class Dominios(db.Model):
    __table__ = db.metadata.tables["dominios"]

    dominio_estado = db.relationship("DominiosEstados", backref="Dominios")
    dominio_tipo_info = db.relationship("DominiosTipos", backref="Dominios")
    
    def __repr__(self):
        return '<Dominios %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_dominio_tipo": self.id_dominio_tipo,
            "id_dominio_estado": self.id_dominio_estado,
            "id_acceso" : self.id_acceso,
            "id_organizacion" : self.id_organizacion,
            "usuario_acceso" : self.usuario_acceso,
            "nombre" : self.nombre,
            "fecha_solicitud" : self.fecha_solicitud,
            "fecha_expiracion" : self.fecha_expiracion,
            "fecha_aprobacion" : self.fecha_aprobacion,
            "fecha_creacion_server" : self.fecha_creacion_server,
            "fecha_renovacion" : self.fecha_renovacion,
            "fecha_inactivacion" : self.fecha_inactivacion,
            "fecha_transferencia" : self.fecha_transferencia,
            "fecha_eliminacion" : self.fecha_eliminacion,
            "parqueo" : self.parqueo,
            "disponible" : self.disponible,
            "exonerado" : self.exonerado,
            "conficker" : self.conficker,
            "controversia" : self.controversia,
            "cant_annos" : self.cant_annos,
            "fecha_creacion" : self.fecha_creacion,
            "fecha_actualizacion" : self.fecha_actualizacion,
            "dominio_estado": self.dominio_estado.toDict(),
            "dominio_tipo_info": self.dominio_tipo_info.toDict(),
        }
    
class DominiosTipos(db.Model):
    
    __table__ = db.metadata.tables["dominios_tipos"]

    dominio_tipo = db.relationship("DominiosTiposAreas", backref="DominiosTipos")
    costos = db.relationship("FacturacionServicios", backref="DominiosTipos", )
    
    def __repr__(self):
        return '<DominiosTipos %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_dominio_tipo_area_profesion": self.id_dominio_tipo_area_profesion,
            "nombre": self.nombre,
            "islock": self.islock,
            "gratis": self.gratis,
            "orden": self.orden,
            "segundo_nivel": self.segundo_nivel,
            "restringido": self.restringido,
            "estatus": self.estatus,
            "dominio_tipo": self.dominio_tipo.toDict(),
            "costos": [r.toDict() for r in self.costos],
        }
        
    def toDictMin(self):
       return {
            "id": self.id,
            "id_dominio_tipo_area_profesion": self.id_dominio_tipo_area_profesion,
            "nombre": self.nombre,
            "islock": self.islock,
            "orden": self.orden,
            "segundo_nivel": self.segundo_nivel,
        }
        
        
class DominiosTiposAreas(db.Model):
    
    __table__ = db.metadata.tables["dominios_tipos_areas"]
       
    def __repr__(self):
        return '<DominiosTiposAreas %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,

        }
        
class DominiosEstados(db.Model):
    
    __table__ = db.metadata.tables["dominios_estados"]
       
    def __repr__(self):
        return '<DominiosEstados %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "alias": self.alias,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,

        }

        
class DominiosDocumentos(db.Model):
    
    __table__ = db.metadata.tables["dominios_documentos"]
       
    def __repr__(self):
        return '<DominiosDocumentos %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_dominio": self.id_dominio,
            "uri": self.uri,
            "size": self.size,
            "nombre": self.nombre,
            "mimetype": self.mimetype,
            "tipo": self.tipo,
            "status": self.status,
            "fecha_creacion": self.fecha_creacion,
        }

class DominiosDns(db.Model):
    
    __table__ = db.metadata.tables["dominios_dns"]
       
    def __repr__(self):
        return '<DominiosDns %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_dominio": self.id_dominio,
            "nombre": self.nombre,
            "orden": self.estatus,
            "fecha_creacion": self.fecha_creacion,
        }
        
class DominiosDnsIP(db.Model):
    
    __table__ = db.metadata.tables["dominios_dns_ip"]
       
    def __repr__(self):
        return '<DominiosDnsIP %r>' % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_dominio_dns": self.id_dominio_dns,
            "ip_servidor": self.ip_servidor,
            "fecha_creacion": self.fecha_creacion,

        }