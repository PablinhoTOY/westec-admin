import os
from . import ControllerObject
from app import *
import requests
import json 

APIKEY = os.getenv("APIKEY")

def GetCountries():
    ret = ControllerObject()
    url = 'https://api.countrystatecity.in/v1/countries'
    headers = {
         'X-CSCAPI-KEY': APIKEY
    }

    respuesta = requests.request('GET', url, headers=headers)
    ret.payload = json.loads(respuesta.text)

    return ret


def GetStatesofCountry(countryIso):
    ret = ControllerObject()
    url = f'https://api.countrystatecity.in/v1/countries/{countryIso}/states'
    # url2 = f'https://api.countrystatecity.in/v1/countries/{countryIso}'
    headers = {
         'X-CSCAPI-KEY': APIKEY
    }

    statesResponse = requests.request('GET', url, headers=headers)
    states = statesResponse.text
    # countryInfoResponse = requests.request('GET', url2, headers=headers)
    # countryInfo = countryInfoResponse.text

    ret.payload = {
        'states':states,
        # 'countryInfo':countryInfo,
    }

    return ret


def GetCitiesbyStateCountry(countryIso, stateIso):
    ret = ControllerObject()
    url = f'https://api.countrystatecity.in/v1/countries/{countryIso}/states/{stateIso}/cities'
    headers = {
         'X-CSCAPI-KEY': APIKEY
    }
    respuesta = requests.request('GET', url, headers=headers)
    
    ret.payload = {
        'payload': json.loads(respuesta.text)
    }

    return ret