from flask import request, make_response, jsonify, abort
from app import app, db
from app.Models.Users import Permisos
from app.util import userIsAdmin, generateResponse, generateError
from . import ControllerObject


def GetAllPermisos():
    ret = ControllerObject()

    try:
        ret.payload = [permisos.as_dict() for permisos in Permisos.query.all()]
    except Exception as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400

    return ret


def SavePermiso(permiso):
    ret = ControllerObject()

    try:
        permiso = Permisos(
            nombre=permiso.get("nombre"),
            categoria=permiso.get("categoria"),
            key=permiso.get("key"),
        )
        db.session.add(permiso)
        db.session.commit()

        app.logger.info("Permiso %s creado exitosamente.", permiso.nombre)
        ret.mensaje = "Permiso añadido exitosamente."

    except Exception as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400

    return ret


def manage_permisos(pid):
    ret = ControllerObject()

    try:
        if request.method == "GET":
            permiso = Permisos.query.get(pid)

            if permiso:
                ret.payload = [Permisos.as_dict(permiso)]
            else:
                ret.mensaje = "El rol no fue encontrado"
                ret.status = 404

        elif request.method == "POST":
            # valid_perms = getValidPermissions(request.json["role_permissions"])
            permiso = Permisos.query.get(pid)

            if int(pid) == 1:
                if permiso and not (permiso.nombre == request.json["nombre"]):
                    ret.mensaje = (
                        "No se puede editar el nombre del permiso de Administrar Todo."
                    )
                    ret.status = 400
                    return ret

            if permiso:
                try:
                    permiso.nombre = request.json["nombre"]
                    permiso.categoria = request.json["categoria"]
                    #  role.permissions = valid_perms
                    db.session.commit()
                    ret.mensaje = "Permiso Modificado"

                except:
                    ret.mensaje = "Faltan campos por añadir"
                    ret.status = 400

            else:
                try:
                    permiso = Permisos(
                        nombre=request.json["nombre"],
                        categoria=request.json["categoria"],
                        # permissions = valid_perms
                    )
                    db.session.add(permiso)
                    db.session.commit()
                    ret.mensaje = "Permiso creado"

                except:
                    ret.mensaje = "Faltan campos por añadir"
                    ret.status = 400

        elif request.method == "DELETE":
            if int(pid) == 1:
                ret.mensaje = "Digo, sé que odias a los administradores, pero no puedes dejar un admin huérfano. Sentido común, por favor."
                ret.status = 400

            else:
                permiso = Permisos.query.get(pid)

                if permiso:
                    db.session.delete(permiso)
                    db.session.commit()
                    ret.mensaje = "Permiso eliminado"

                else:
                    ret.mensaje = "No se encontró el permiso solicitado"
                    ret.status = 404

    except Exception as err:
        ret.mensaje = "No se puede completar la solicitud."
        ret.status = 400

    return ret
