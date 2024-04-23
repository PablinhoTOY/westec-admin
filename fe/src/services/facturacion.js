
import { ApiService } from "./api.config";

export const getOrder = async () => {
    return ApiService.get("getOrder")
      .then(response => response.data)
      .catch(response => Promise.resolve(response))
  }

  export const getCostos = async () => {
    return ApiService.get("costos")
      .then(response => response.data)
      .catch(response => Promise.resolve(response))
  }

  export const getCostosDominio = async (tipo) => {
    return ApiService.get(`costos/${tipo}`)
      .then(response => response.data)
      .catch(response => Promise.resolve(response))
  }

export const GetAllFacturas = () => {
  return new Promise(async resolve => {
    return ApiService.get('/facturas')
      .then((response) => {
        resolve(response.data)
      })
      .catch(({ response }) => {
        resolve(response)
      })
  })
}

export const pagoCredito = async (data) => {
  return ApiService.post("pago/PagoCredito", data)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}


