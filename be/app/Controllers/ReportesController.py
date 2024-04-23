from datetime import date

from flask import make_response, render_template
from app import app, db
from app.Models.Users import User, Role, Permisos
from app.Models.Dominios import Dominios
from app.pdf import final_pdf
from . import ControllerObject

from sqlalchemy import func
import sqlalchemy


from app.util import userIsAdmin, generateResponse, generateError

from pandas import DataFrame

######## Usuarios ###################
def reportes_custom_usuario(condiciones):
#Valores a recibir:
#Fecha de creación, último login, roles, grupo.
    my_filters = {}
    if condiciones.get('active'):
        my_filters['active'] = condiciones.get('active')
    if condiciones.get('grupo_id'):
        my_filters['grupo_id'] = condiciones.get('grupo_id')
    if condiciones.get('fecha_creacion'):
        my_filters['fecha_creacion'] = condiciones.get('fecha_creacion')
    if condiciones.get('fecha_comparacion'):
        my_filters['fecha_comparacion'] = condiciones.get('fecha_comparacion')
    if condiciones.get('roles'):
        my_filters['roles'] = condiciones.get('roles')
    usuarios = User.query
    
    for attr,value in my_filters.items():
        if attr == 'active':
            usuarios = usuarios.filter(getattr(User,attr)==value )
        if attr == 'grupo_id':
            usuarios = usuarios.filter(getattr(User,attr)==value )
        if attr == 'fecha_creacion':
            usuarios = usuarios.filter(getattr(User,attr).between(value, condiciones.get('fecha_comparacion')))
        #if attr == 'roles':
        #    usuarios = usuarios.filter(User.roles.any(Role.id.in_(value)))
        #    print(usuarios.filter(User.roles.any(Role.id.in_(value))))
     
    results = usuarios.all()
    if results:
        df = DataFrame(usuarios.toDict() for usuarios in usuarios)
        resp = make_response (df.to_csv(index=False, encoding='utf-8'))
        resp.headers["Content-Disposition"] = "attachment; filename=usuariosreporte.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp
    else:
        return generateError('Error', 404, "No se encontraron resultados.")
# Reporte Historial Dominio


def getHistorialDominio():
    ret = ControllerObject()
    q = Dominios.query

    ret.payload = [{"id":t.id, "nombre":t.nombre} for t in q]
    return ret