import datetime
import json
from flask_login import current_user
from app import app
from flask import make_response
from app.Controllers import (
    UsersController as users,
    UserInfoController as userinfo,
    RolesController as roles,
    GrupoController as grupos,
    PermisosController as permisos,
    ReportesController as reportes,
    FacturacionController as factura,
    DominiosController as dominios,
    PaisesController as paises,
    PagoController as pagos,
)

from flask import jsonify, request, Response, render_template, url_for
import pandas as pd
import requests
from urllib.parse import urlparse


##########################################
##########################################
#########  EndPoints de AuthUser #########
##########################################
##########################################

@app.route("/users", methods=["GET"])
def GetAllUsers():
    result = users.GetAllUsers()
    return result.jsonify()


@app.route("/user/login", methods=["POST"])
def LoginUser():
    result = users.LoginUser(request.get_json(force=True))
    return result.jsonify()


@app.route("/user/register", methods=["POST"])
def RegisterUser():
    result = users.RegisterUser(request.get_json(force=True))
    return result.jsonify()


@app.route("/users/accesos", methods=["GET"])
def GetAccesos():
    result = users.GetAccesos()
    return result.jsonify()

@app.route("/users/sendmailrecoverpassword", methods=["POST"])
def SendMailRecoverPassword():
    result = users.SendMailRecoverPassword(request.get_json(force=True))
    return result.jsonify()

@app.route("/users/resetpassword", methods=["POST"])
def ResetPassword():
    result = users.ResetPassword(request.get_json(force=True))
    return result.jsonify()


@app.route("/users/password/<uid>", methods=['POST'])
def CambiarPassword(uid):
    result = users.change_pass(uid)
    return result.jsonify()

##########################################
##########################################
#########  EndPoints de Userinfo #########
##########################################
##########################################

@app.route("/userinfo/contactos", methods=["POST"])
def GetContactosUser():
    result = userinfo.GetContactosUser(request.get_json(force=True))
    return result.jsonify()

@app.route("/userinfo/areasempresas", methods=["GET"])
def GetTiposAreasEmpresas():
    result = userinfo.GetTiposAreasEmpresas()
    return result.jsonify()

@app.route("/userinfo/ubicaciones", methods=["GET"])
def getUbicaciones():
    result = userinfo.getUbicaciones()
    return result.jsonify()

@app.route("/userinfo/ubicacion/<locale>/<id>", methods=["GET"])
def getUbicacion(locale,id):
    result = userinfo.getUbicacion(locale, id)
    return result.jsonify()


@app.route("/userinfo/identificadores", methods=["GET"])
def getTiposIdentificadores():
    result = userinfo.getTiposIdentificadores()
    return result.jsonify()





##########################################
##########################################
#########  EndPoints de Roles ############
##########################################
##########################################


@app.route("/roles", methods=["GET"])
@app.route("/roles/", methods=["GET"])
def Roles():
    result = roles.GetAllRoles()
    return result.jsonify()

@app.route("/roles/<rid>", methods=["GET", "POST", "DELETE"])
def RolTodos(rid):
    result = roles.manage_roles(rid)
    return result.jsonify()

@app.route("/roles", methods=["POST"])
@app.route("/roles/", methods=["POST"])
def SaveRoles():
    result = roles.SaveRole(request.get_json(force=True))
    return result.jsonify()


##########################################
##########################################
#######  EndPoints de Permisos  ##########
##########################################
##########################################


@app.route("/permisos", methods=["GET"])
@app.route("/permisos/", methods=["GET"])
def Permisos():
    result = permisos.GetAllPermisos()
    return result.jsonify()

@app.route("/permisos", methods=["POST"])
@app.route("/permisos/", methods=["POST"])
def SavePermiso():
    result = permisos.SavePermiso(request.get_json(force=True))
    return result.jsonify()

@app.route("/permisos/<pid>", methods=["GET", "POST", "DELETE"])
def PermisosTodos(pid):
    result = permisos.manage_permisos(pid)
    return result.jsonify()


##########################################
##########################################
#######  EndPoints de Permisos Roles  ##########
##########################################
##########################################


@app.route("/role-permisos", methods=["GET"])
def ObtenerPermisoRol():
    result = roles.getallPermisosRoles()
    return result.jsonify()

@app.route("/role-permisos", methods=["POST"])
def InsertarPermisoRol():
    result = roles.añadirPermisos(request.json["datos"])
    return result.jsonify()


##########################################
##########################################
#########  EndPoints de Grupos ###########
##########################################
##########################################

@app.route("/grupos/list", methods=["GET"])
def GetGruposList():
    result = grupos.GetAllGrupos()
    return result.jsonify()

@app.route("/grupos", methods=["POST"])
def SaveGrupos():
    result = grupos.SaveGrupo(request.json)
    return result.jsonify()

@app.route("/grupos/<int:grupo_id>", methods=["DELETE"])
def BorrarGrupos(grupo_id):
    result = grupos.BorrarGrupo(grupo_id)
    return result.jsonify()

@app.route("/grupos-usuario/<int:grupo_id>", methods=["GET"])
def GetGrupoUsuarios(grupo_id):
    result = grupos.GrupoUsuarios(grupo_id)
    return result.jsonify()


##########################################
##########################################
#########  EndPoints de Facturacion ######
##########################################
##########################################

@app.route("/facturas", methods=["GET"])
def getAllfacturas():
    result = factura.getAllFacturas()
    return result.jsonify()

@app.route("/costos", methods=["GET"])
def GetAllCostos():
    result = factura.GetAllCostos()
    return result.jsonify()

@app.route("/costos-tipo/<dominio>", methods=["GET"])
def GetCostoDominioTipo(dominio):
    result = factura.GetCostoDominioTipo(dominio)
    return result.jsonify()


##########################################
##########################################
#########  EndPoints de Dominios ###########
##########################################
##########################################
@app.route("/dominios/listaCompleta", methods=["GET"])
def GetAllDominios():
    result = dominios.GetAllDominios()
    return result.jsonify()

@app.route("/dominios/tipos", methods=["GET"])
def GetAllTiposDominios():
    result = dominios.GetAllTiposDominios()
    return result.jsonify()

@app.route("/dominios/buscarDominio", methods=["POST"])
def GetDominioBuscado():
    result = dominios.GetDominioBuscado(request.get_json(force=True))
    return result.jsonify()

@app.route("/dominios/usuario", methods=["POST"])
def GetDominiosUsuario():
    result = dominios.GetDominiosUsuario(request.get_json(force=True))
    return result.jsonify()

@app.route("/dominios/cotizar-dominio", methods=["POST"])
def CotizarDominio():

    dominiosData = json.loads(request.form.get('dominios'))
    userdata = json.loads(request.form.get('userdata'))
    files = request.files.getlist('files')

    result = dominios.CotizarDominio(dominiosData, userdata, files)
    return result.jsonify()

##########################################
##########################################
#########  EndPoints de Paises ###########
##########################################
##########################################


@app.route("/countries", methods=["GET"])
def GetCountries():
    result = paises.GetCountries()
    return result.jsonify()

@app.route("/country/<countryIso>", methods=["GET"])
def GetStatesofCountry(countryIso):
    result = paises.GetStatesofCountry(countryIso)
    return result.jsonify()

@app.route("/country/<countryIso>/state/<stateIso>", methods=["GET"])
def GetCitiesbyStateCountry(countryIso, stateIso):
    result = paises.GetCitiesbyStateCountry(countryIso, stateIso)
    return result.jsonify()

#####################################################
#####################################################
#########  EndPoints de Pagos y consultas ###########
#####################################################
#####################################################

@app.route("/getPrice/<domain>", methods=["GET"])
def getPrice(domain):
    result = pagos.getPrice(domain)
    return result.jsonify()


@app.route("/pago/PagoCredito", methods=["POST"])
def PagoCredito():
    result = pagos.PagoCredito(request.get_json(force=True))
    return result.jsonify()






@app.route("/pruebaendpointxd", methods=["get"])
def PruebaEndpoint():
    result = pagos.PruebaEndpoint()
    return result.jsonify()
