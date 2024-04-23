import os
import secrets
from PIL import Image
from app import app
from app.modules.funciones_extras.funciones import verificar_ruta


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)

    output_size = (200, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def save_picture_docente(foto, cedula):
    random_hex = secrets.token_hex(5)
    _, f_ext = os.path.splitext(foto.filename)
    filename = "{}-{}{}".format(cedula, random_hex, f_ext)

    path = os.path.join(app.root_path, "static/docentes_images")
    verificar_ruta(path)
    foto.save(os.path.join(path, filename))

    output_size = (400, 500)
    i = Image.open(foto)
    i.thumbnail(output_size)
    i.save(os.path.join(path, filename))

    return filename
