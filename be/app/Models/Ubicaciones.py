from app import app, db
from functools import wraps
import uuid
from datetime import datetime

with app.app_context():
    db.reflect()

class PaisesUbicaciones(db.Model):
    __table__ = db.metadata.tables["ubicaciones"]

    def __repr__(self):
        return "<PaisesUbicaciones %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "cctld": self.cctld,
            "abreviatura": self.abreviatura,
            "nombre": self.nombre,
            "nombre_en": self.nombre_en,
            "codigo_telefonico": self.codigo_telefonico,
            "idioma": self.idioma,   
        }