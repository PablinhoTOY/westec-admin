import { ApiService } from "./api.config";

export const ObtenerListadoRoles = async () => {
  return ApiService.get("roles")
    .then(response => response.data)
    .catch(response => Promise.resolve(response))
}

export const SaveRol = async (rol) => {
  return ApiService.post('roles', rol)
  .then(response => response.data)
  .catch(response => Promise.resolve(response))
}

export const actualizarrolPermisos = async (rol) => {
  return ApiService.post('role-permisos', rol)
  .then(response => response.data)
  .catch(response => Promise.resolve(response))
}

export const UpdateRol = async (id, rol) => {
  return ApiService.post('roles/' + id, rol)
  .then(response => response.data)
  .catch(response => Promise.resolve(response.response))
}

export const DeleteRol = async (did) => {
  return ApiService.delete('roles/' + did)
  .then(response => response.data)
  .catch(response => Promise.resolve(response.response))
}