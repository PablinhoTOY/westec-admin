from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.sql import func
from app import app, db
from flask import abort, flash, jsonify, make_response, request
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_security import UserMixin, RoleMixin
from functools import wraps
import uuid
import jwt
from datetime import datetime
from sqlalchemy.orm import backref


# @login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    # password = db.Column(db.String(128), nullable=False)
    profile_image = db.Column(
        db.String(255), nullable=False, default="default_portrait.png"
    )
    fecha_creacion = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.Text, unique=True, nullable=True)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary = 'roles_users', backref="user", lazy="select")
    grupo_id = db.Column(
        db.Integer, db.ForeignKey("grupos.id", ondelete="CASCADE"), nullable=False
    )
    grupo = db.relationship("Grupo", backref="user")

  #  def __init__(self, *args, **kwargs):
  #      if "password" in kwargs:
  #          kwargs["password"] = generate_password_hash(kwargs["password"])
  #      super(User, self).__init__(*args, **kwargs)
        
        
    def __repr__(self):
        return '<User %r>' % self.id

    def toDict(self):
        
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "active": self.active,
            "grupo": self.grupo.nombre,
            "roles": [r.name for r in self.roles],
            "grupo_id": self.grupo_id,
            "fecha_creacion": self.fecha_creacion,
            "last_login": self.last_login_at,
        }

    def get_reset_token(self, expires_sec=600):
        s = Serializer(app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

   # def check_password(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
   #     return check_password_hash(self.password_hash, password)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        # return 401 if token is not passed
        if not token:
            return jsonify({"message": "Token is missing !!"}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
            current_user = User.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"message": "Token is invalid !!"}), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated

roles_users = db.Table(
    "roles_users",
    db.Column("usuario_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
)

role_permission = db.Table(
    "role_permission",
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
    db.Column("permission_id", db.Integer, db.ForeignKey("permisos.id")),
)
class Role(db.Model, RoleMixin):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    permisos = db.relationship('Permisos', secondary = 'role_permission', backref="role", lazy=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now()
    )
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now()
    )

    def as_dict(self):
        return {"id": self.id, "name": self.name,"permisos": [r.as_dict() for r in self.permisos]}

    def __repr__(self):
        return '<Role %r>' % self.id
    

class Estados(db.Model):
    __tablename__ = "estados"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    flag = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now()
    )
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now()
    )

    def __repr__(self):
        return "<Estado '{}'>".format(self.nombre)

    def as_dict(self):
        return {"id": self.id, "nombre": self.nombre, "flag": self.flag}


class Permisos(db.Model):
    __tablename__ = "permisos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text, nullable=False)
    key = db.Column(db.String(10), nullable=False)
    categoria = db.Column(db.String(255), nullable=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now()
    )
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
    
    def __repr__(self):
        return '<Permission %r>' % self.id

    def as_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "key":self.key
        }

class Usuario_token(db.Model):
    __tablename__ = "usuario_token"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    uid = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    token = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime(timezone=True), default=func.now())
    fecha_expiracion = db.Column(db.DateTime(timezone=True), nullable=True)
    estado = db.Column(db.Boolean, nullable=False)

    #  role = db.relationship("Roles", backref=db.backref(
    #      "roles_permission", cascade="all, delete-orphan"))

    def as_dict(self):
        return {
            "token": self.token,
            "fecha_creacion": self.fecha_creacion,
            "estado": self.estado,
        }


