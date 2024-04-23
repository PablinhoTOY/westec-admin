from flask import request, make_response, jsonify, abort
from app import app, db
from app.Models.Users import Role, role_permission, Permisos
from app.util import userIsAdmin, generateResponse, generateError
from . import ControllerObject

def GetAllRoles():
    ret = ControllerObject()

    try:
        ret.payload = [roles.as_dict() for roles in Role.query]
    except (Exception):
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret

def SaveRole(role):
    ret = ControllerObject()

    try:
        rol = Role(name=role.get("name"))
        db.session.add(rol)
        db.session.commit()

        app.logger.info("Rol %s creado exitosamente.", role.get("name"))
        ret.mensaje = "Rol Creado"
        
    except (Exception) as err:
        ret.mensaje = "No se puede completar la solicitud."
        ret.status = 400
    
    return ret

def manage_roles(data):
    ret = ControllerObject()

    try:
        if request.method == 'GET':
            role = Role.query.get(data)

            if role:
                ret.payload = [Role.as_dict(role)]
            else:
                ret.mensaje = "El rol no fue encontrado"
                ret.status = 404
            
        elif request.method == 'POST':
           # valid_perms = getValidPermissions(request.json["role_permissions"])
            role = Role.query.get(data)
            print(role)
            
            if int(data) == 1:
                if role and not (role.name == request.json["name"]):
                    ret.mensaje = "No se puede modificar el rol Admin."
                    ret.status = 400
                    return ret
                
            if role:
                role.name = request.json["name"]
                #  role.permissions = valid_perms

                db.session.commit()
                ret.mensaje = "Rol Modificado"
            
            else:
                role = Role(
                    name=request.json["name"],
                    # permissions = valid_perms
                )

                db.session.add(role)
                db.session.commit()
                ret.mensaje = "Rol creado"
                
        elif request.method == 'DELETE':
            if int(data) == 1:
                ret.mensaje = "Cómo deseas borrar un admin? No digas algo absurdo"
                ret.status = 400
            
            else:
                role = Role.query.get(data)

                if role:
                    db.session.delete(role)
                    db.session.commit()
                    ret.mensaje = "Rol eliminado"
                
                else:
                    ret.mensaje = "No se encontró el rol solicitado"
                    ret.status = 404
    
    except (Exception) as err:
        ret.mensaje = "No se puede completar la solicitud."
        ret.status = 400
    
    return ret
        
            
def getValidPermissions(IDarr):
    perms = []

    for perm_id in IDarr:
        perm = Permisos.query.filter_by(id=perm_id).first()

        if (not (perm is None)):
            perms.append(perm)

    return perms

def getallPermisosRoles():
    results = []

    for r in Role.query:
        results.append({
            "role": r.id,
            "permisos": [p.id for p in r.permisos],
        })
    
    return ControllerObject(payload=results)
    
def añadirPermisos(parametros):
    ret = ControllerObject()
    
    try:
        for param in parametros:
            rid = param.get('role')
            if rid:
                role = Role.query.filter_by(id=rid).first()
                del role.permisos[:] 
                db.session.commit()
                
                for val in param.get('permisos'):
                    permiso = Permisos.query.filter_by(id=val).first()
                    role.permisos.append(permiso)
            else:
                raise TypeError
        
        db.session.commit()
        ret.mensaje = "Se añadieron los permisos al rol"
    
    except TypeError as e:
        db.session.rollback()
        ret.mensaje = "Hubo un error en la solicitud."
        ret.status = 400
    
    return ret
 