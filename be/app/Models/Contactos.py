from app import app, db
from functools import wraps
import uuid
from datetime import datetime
from app.Models.Dominios import Dominios

with app.app_context():
    db.reflect()

class Contactos(db.Model):
    __table__ = db.metadata.tables["contactos"]

    # Define relationships
    contactos_dominios = db.relationship("ContactosDominios", backref="contactos")
    area_empresa = db.relationship("TiposAreasEmpresas", backref="contactos", primaryjoin='TiposAreasEmpresas.id == Contactos.id_tipo_area_empresa', foreign_keys="Contactos.id_tipo_area_empresa",)
    
    def __repr__(self):
        return "<Contactos %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_acceso": self.id_acceso,
            "id_tipo_identificacion": self.id_tipo_identificacion,
            "id_tipo_area_empresa": self.id_tipo_area_empresa,
            "id_contacto_tipo" : self.id_contacto_tipo,
            "id_ubicacion": self.id_ubicacion,
            "nombre": self.nombre,
            "apellido": self.apellido,
            #"identificacion": self.identificacion,
            #"empresa": self.empresa,
            "cargo": self.cargo,
            "direccion1": self.direccion1,
            "direccion2": self.direccion2,
            "ciudad": self.ciudad,
            "estado": self.estado,
            #"pais": self.pais,
            "email": self.email,
            "telefono": self.telefono,
            "favorito" : self.favorito,
            "representante_legal": self.representante_legal,
            "idioma": self.idioma,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,
            "fecha_actualizacion": self.fecha_actualizacion,
            "contactos_dominios": [r.toDict() for r in self.contactos_dominios],
            "area_empresa": self.area_empresa.toDict()
        }

class ContactosDominios(db.Model):
    __table__ = db.metadata.tables["contactos_dominios"]

    contactos_roles = db.relationship("ContactosRoles", backref="contactos_dominios")

    def __repr__(self):
        return "<ContactosDominios %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "nombre_dominio": Dominios.query.filter(self.id_dominio==Dominios.id).with_entities(Dominios.nombre).scalar(),
            "codigo_contacto" : self.codigo_contacto,
            "fecha_creacion": self.fecha_creacion,   
            "tipo_contacto": self.contactos_roles.toDict(),
        }

class ContactosRoles(db.Model):
    __table__ = db.metadata.tables["contactos_roles"]

    def __repr__(self):
        return "<ContactosRoles %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,   
        }

class TiposAreasEmpresas(db.Model):
    __table__ = db.metadata.tables["tipos_areas_empresas"]
    
    def __repr__(self):
        return "<TiposAreasEmpresas %r>" % self.id
    
    def toDict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }