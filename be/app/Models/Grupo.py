from app import db
from datetime import datetime


class Grupo(db.Model):
    __tablename__ = "grupos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False, unique=True)
    codigo = db.Column(db.Integer, nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now()
    )
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
    
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def toDict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "codigo": self.codigo,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def toList(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
