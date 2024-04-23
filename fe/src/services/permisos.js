import { ApiService } from "./api.config";

export const ObtenerListadoPermisos = () => {
  return new Promise(async resolve => {
    return ApiService.get("permisos")
      .then((response) => {
        resolve(response.data);
      })
      .catch(({ response }) => {
        resolve(response);
      });
  });
}

export const SavePermiso = (permiso) => {
  return new Promise(async resolve => {
    return ApiService.post('permisos', permiso)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}

export const UpdatePermiso = (id, permiso) => {
  return new Promise(async resolve => {
    return ApiService.post('permisos/' + id, permiso)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}

export const DeletePermiso = (did) => {
  return new Promise(async resolve => {
    return ApiService.delete('permisos/' + did)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}