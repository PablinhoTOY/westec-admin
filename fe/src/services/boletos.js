import { ApiService } from "./api.config";

export const ObtenerTodasOrdenes = async () => {
  return ApiService.get("ordenes")
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const GuardarOrden = async (orden) => {
  return ApiService.post("orden", { orden: orden })
    .then(response => response.data)
    .catch(response => Promise.resolve(response.response))
}

export const AceptarOrden = async (orden) => {
  return ApiService.post("orden/aceptar", orden)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const BorrarOrden = async (ordenId) => {
  return ApiService.delete("orden/" + ordenId)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const ObtenBoletosDisponibles = async (grupo_id) => {
  return ApiService.get(`boletos/disponibles/${grupo_id}`)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const ObtenBoletosDisponiblesUsuario = async (usuario_id) => {
  return ApiService.get(`boletos/disponibles-usuario/${usuario_id}`)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const ObtenAsignacionTrabajador = async (usuario_id) => {
  return ApiService.get(`boletos/asignacion-boletos/${usuario_id}`)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}
