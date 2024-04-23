import axios from 'axios'
import {
  useUserStore
} from '../stores/user'

export const serverIP = "http://localhost:5000"
//export const serverIP = "https://192.168.10.150:8080"

export const ApiService = axios.create({
  baseURL: serverIP,
  headers: {
    'who': getToken()
  }
})

export const IntegradorService = axios.create({
  baseURL: 'https://pdi.utp.ac.pa/api/endpoint/public?cmd=utp-unidades',
})

function getToken() {
  var user = window.localStorage.user;
  if (user != undefined) return JSON.parse(user).id
  return 0;
}
