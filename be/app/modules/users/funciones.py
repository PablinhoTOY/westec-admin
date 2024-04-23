from threading import Timer
import os, re
from pathlib import Path
from PIL import Image

from flask import jsonify, make_response, request
import jwt
from app.Models.Users import User, Role, Usuario_token
from app import db, app

from datetime import datetime, timedelta
from flask_security import (
    SQLAlchemyUserDatastore,
    Security,
    login_user,
    current_user,
    logout_user,
)


userdata = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, userdata)


def crear_token_db(uid, token, fecha_creacion, fecha_expiracion, estado):
    my_data = Usuario_token(uid, token, fecha_creacion, fecha_expiracion, estado)
    db.session.add(my_data)
    db.session.commit()
    token_timer(uid)


def actualizar_token_db(uid, token, fecha_creacion, fecha_expiracion, estado):
    my_data = Usuario_token.query.filter_by(uid=uid).first()
    my_data.token = token
    my_data.fecha_creacion = fecha_creacion
    my_data.fecha_expiracion = fecha_expiracion
    my_data.estado = estado
    db.session.commit()


def desactivar_token(uid):
    estado = False
    my_data = Usuario_token.query.filter_by(uid=uid).first()
    my_data.estado = estado
    db.session.commit()


def token_timer(uid):
    total_seconds = 86400
    timer = Timer(total_seconds, desactivar_token, args=(uid,))
    timer.start()


def get_jwt_token(user):
    exp = datetime.now() + timedelta(hours=24)
    key = app.config["SECRET_KEY"]
    payload = {
        "id": user.id,
        "exp": datetime.now() + timedelta(hours=24),
    }
    token = jwt.encode(payload, key, algorithm="HS256")

    return token, exp


def verificar_ruta(directorio):
    try:
        os.stat(directorio)
    except:
        os.mkdir(directorio)
    
    return directorio
    


def revisar_archivo_existe(path_file):

    file = Path(path_file)
    return file.is_file()

def save_picture_menus(foto):
    filename = foto.filename
    root = verificar_ruta(os.path.join(app.root_path, 'static'))
    path = verificar_ruta(os.path.join(app.root_path, 'static/menus'))

    foto.save(os.path.join(path, filename))

    output_size = (600, 800)
    i = Image.open(foto)
    i.thumbnail(output_size)
    i.save(os.path.join(path, filename))

    return filename