import os
import re
import datetime
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    decode_token,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)
from jwt import DecodeError, ExpiredSignatureError
import requests
import json
from flask import (
    make_response,
    render_template,
    url_for,
    flash,
    redirect,
    request,
    Blueprint,
    jsonify,
)
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import or_
from flask_security import current_user
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_mail import Message
from app import *


from werkzeug.security import generate_password_hash, check_password_hash
from webargs import flaskparser, fields

from app.Models.Users import (
    # Role_Permisos,
    User,
    Role,
    Permisos,
    Usuario_token,
)
from flask_security import (
    SQLAlchemyUserDatastore,
    Security,
    login_user,
    current_user,
    logout_user,
)


from app.modules.users.funciones import *
from app.modules.users.funciones import security


users = Blueprint("users", __name__)

FORM_ARGS = {
    "email": fields.Email(required=True),
    "username": fields.Str(required=True),
}


@users.route("/user", methods=["GET", "POST"])
@users.route("/acceder", methods=["GET", "POST"])
def login():
    email = request.json["email"]
    try: token = json.loads(request.json["password"])
    except: token = None

    user = User.query.filter_by(email=email).first()
    
    if user and user.active == 1 and token:
        r = requests.post("https://sso.utp.ac.pa/ms/user", json=token)
        js = r.json()

        if email == js["mail"]:
            login_user(user=user)
            db.session.commit()
            access_token = token["access_token"]

            response = jsonify(
                {
                    "token": access_token,
                    "nombre": user.nombre,
                    "apellido": user.apellido,
                    "id": user.id,
                    "grupo_id": user.grupo_id,
                    "email": user.email,
                    "title": "Success",
                    "mensaje": "Iniciaste sesión",
                    "route": getInitialRouteByUser(user.roles),
                    "permisos": PermisosRolesByUser(user.roles),
                }
            )
            return response, 200
    
    return (
        jsonify({"title": "Error", "mensaje": "Usuario o contraseña incorrecta."}),
        401,
    )

def PermisosRolesByUser(roles):
    permisos = []
    for rol in roles:
        permisos.append(
            {
                "role": rol.as_dict().get("id"),
                # "permisos":rol.as_dict().get("permisos")
                "permisos": [p.key for p in rol.permisos],
            }
        )

    return permisos


def getInitialRouteByUser(roles):
    for rol in roles:
        rolId = rol.as_dict().get("id")
        return "/"


@users.route("/logout")
def logout():
    # desactivar_token(id)
    app.logger.info("%s cerró sesión", current_user.username)
    response = jsonify()
    unset_jwt_cookies(response)
    logout_user()

    return jsonify({"title": "Cerrar sesión", "mensaje": "saliste"}), 200


# -----------------------------------------------------------------------
# -----------------------------Usuarios-------------------------------
# -----------------------------------------------------------------------


def send_reset_email(user, token):
    msg = Message()
    msg.subject = "Solicitud de Reinicio de Contraseña"
    msg.sender = '"Cárnet UTP" <bolsadetrabajo@utp.ac.pa>'
    msg.recipients = [user.email]
    msg.html = render_template(
        "correos/reset_password.html",
        user=user,
        token=token,
        domain=os.getenv("SERVER"),
    )

    mail.send(msg)


def send_pass_confirmation_email_reset(user):
    msg = Message()
    msg.subject = "Modificación de Contraseña"
    msg.sender = '"Cárnet UTP" <bolsadetrabajo@utp.ac.pa>'
    msg.recipients = [user.email]
    msg.html = render_template("correos/changed_password.html", user=user)

    mail.send(msg)


