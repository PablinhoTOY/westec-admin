import { ApiService } from "./api.config";

export const ObtenerListadoPermisosRoles = async () => {
      return ApiService.get("role-permisos")
        .then(response => response.data)
        .catch(response => Promise.resolve(response))
  }

export const SavePermisoRol = async (pedido) => {
  return ApiService.post('role-permisos', {datos:pedido})
  .then(response => response.data)
  .catch(response => Promise.resolve(response))
}