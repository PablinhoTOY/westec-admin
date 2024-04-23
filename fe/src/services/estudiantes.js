import { ApiService } from "./api.config";

export const ObtenerEstudiante = async (cedula) => {
  return ApiService.get("estudiante?cedula=" + cedula)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const ObtenerEstudianteToken = async (token) => {
  return ApiService.get("estudiante?token=" + token)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const GuardarAsignacionBoleto = async (detalles, grupo_id) => {
  return ApiService.post(`estudiante/asignar/${grupo_id}`, detalles)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const ConsumirBoleto = async (estudiante) => {
  return ApiService.post("estudiante/consumir", estudiante)
    .then(response => response.data)
    .catch(response => Promise.resolve(response.response.data))
}

export const ObtenerEstudiantes = async (grupo_id) => {
  return ApiService.get(`estudiantes/${grupo_id}`)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const GuardarEstudiantesData = async (data) => {
  return ApiService.post('estudiantes/save', data)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const ObtDataEstudiante = async (id) => {
  return ApiService.get(`estudiante/data/${id}`)
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}