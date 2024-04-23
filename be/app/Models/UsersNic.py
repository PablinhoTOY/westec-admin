from app import app, db
from functools import wraps
import uuid
from datetime import datetime
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer

with app.app_context():
    db.reflect()


class UsuariosExternos(db.Model):
    __table__ = db.metadata.tables["usuarios_externos"]

    def __repr__(self):
        return "<UsuariosExternos %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "id_acceso": self.id_acceso,
            "id_tipo_cliente": self.id_tipo_cliente,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "tipo_identificacion": self.tipo_identificacion,
            "identificacion": self.identificacion,
            "nacionalidad": self.nacionalidad,
            "ruc_cedula": self.ruc_cedula,
            "empresa": self.empresa,
            "cargo": self.cargo,
            "direccion1": self.direccion1,
            "direccion2": self.direccion2,
            "ciudad": self.ciudad,
            "estado": self.estado,
            "id_ubicacion": self.id_ubicacion,
            "email_alterno": self.email_alterno,
            "telefono": self.telefono,
            "telefono_oficina": self.telefono_oficina,
            "representante_legal": self.representante_legal,
            "idioma": self.idioma,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,
            "fecha_actualizacion": self.fecha_actualizacion,
        }


class AccesoUsuarios(db.Model):
    __table__ = db.metadata.tables["accesos"]

    def __repr__(self):
        return "<AccesoUsuarios %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "email": self.email,
            "contrasena": self.contrasena,
            "cambiar_contrasena": self.cambiar_contrasena,
            "estatus": self.estatus,
            "fecha_creacion": self.fecha_creacion,
        }

    def get_reset_token(self):
        s = Serializer(app.config["SECRET_KEY"], salt="reset-pass-Westec ")
        return s.dumps({"user_id": self.id})

    @staticmethod
    def verify_reset_token(token, max_age=600):
        s = Serializer(app.config["SECRET_KEY"], salt="reset-pass-Westec ")
        try:
            user_id = s.loads(token, max_age=max_age)["user_id"]
        except:
            return None
        return AccesoUsuarios.query.get(user_id)


class TiposIdentificadores(db.Model):
    __table__ = db.metadata.tables["tipos_identificaciones"]

    def __repr__(self):
        return "<TiposIdentificadores %r>" % self.id

    def toDict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
