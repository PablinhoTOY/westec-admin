import os
from flask import request, render_template
from app import app
from sqlalchemy.exc import IntegrityError, DataError, NoResultFound

#from app.Models.UsersNic import UsuariosExternos, AccesoUsuarios
from app.Models.Contactos import Contactos, TiposAreasEmpresas
from app.Models.Ubicaciones import PaisesUbicaciones
from app.Models.UsersNic import TiposIdentificadores
#from app.Models.Dominios import Dominios

from . import ControllerObject

from app import *   

import json
import base64
from datetime import datetime

def GetContactosUser(user):
    ret = ControllerObject()

    userId = user.get('userId')

    if True:
        contactos = [contacto.toDict() for contacto in db.session.query(Contactos)\
                                .filter(Contactos.id_acceso == userId)\
                                .join(TiposAreasEmpresas, Contactos.id_tipo_area_empresa == TiposAreasEmpresas.id)\
                                .all()]
        

  
    ret.payload = contactos
    ret.mensaje = 'Se realizo la consulta exitosamente'
    ret.status = 200

    # except (Exception) as err:
    #     ret.mensaje = "No se pudo realizar la consulta."
    #     ret.status = 400
    
    return ret

def GetTiposAreasEmpresas():
    
    ret = ControllerObject()

    try:
        tiposAreasEmpresas = [contacto.toDict() for contacto in\
                              db.session.query(TiposAreasEmpresas)\
                              .all()]
        
        ret.payload = tiposAreasEmpresas
        ret.mensaje = 'Se realizo la consulta exitosamente'
        ret.status = 200

    except (Exception) as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret

def getUbicaciones():
    
    ret = ControllerObject()

    try:
        ubicaciones = [ubicacion.toDict() for ubicacion in\
                              db.session.query(PaisesUbicaciones)\
                              .all()]
        
        ret.payload = ubicaciones
        ret.mensaje = 'Se realizo la consulta exitosamente'
        ret.status = 200

    except (Exception) as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret

def getUbicacion(locale, id):
    
    ret = ControllerObject()

    try:
        if locale == 'es':
            ubicacion = PaisesUbicaciones.query.filter(id==PaisesUbicaciones.id)\
                                               .with_entities(PaisesUbicaciones.nombre).scalar()
        else: 
            ubicacion = PaisesUbicaciones.query.filter(id==PaisesUbicaciones.id)\
                                               .with_entities(PaisesUbicaciones.nombre_en).scalar()
        
        ret.payload = ubicacion
        ret.mensaje = 'Se realizo la consulta exitosamente'
        ret.status = 200

    except (Exception) as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret

def getTiposIdentificadores():

    ret = ControllerObject()

    try:
        identificaciones = [identificacion.toDict() for identificacion in\
                              db.session.query(TiposIdentificadores)\
                              .all()]
        
        ret.payload = identificaciones
        ret.mensaje = 'Se realizo la consulta exitosamente'
        ret.status = 200

    except (Exception) as err:
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret