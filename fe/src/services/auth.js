import {
  ApiService
} from "./api.config";

export const Loguear = async (credenciales) => {
  return ApiService.post("user", credenciales)
    .then(response => resolve(response))
    .catch(response => resolve(response))
}

export const Desloguear = (userID) => {
  return new Promise(async resolve => {
    return ApiService.post("logout/" + userID, credenciales)
      .then((response) => {
        resolve(response);
      })
      .catch(({
        response
      }) => {
        resolve(response);
      });
  });
}

export const Registrar = (registro) => {
  return new Promise(async resolve => {
    return ApiService.post("registro", registro)
      .then((response) => {
        resolve(response);
      })
      .catch(({
        response
      }) => {
        resolve(response);
      });
  });
}

export const CambiarContrasena = (credenciales) => {
  return new Promise(async resolve => {
    return ApiService.put("contrasena", credenciales)
      .then((response) => {
        resolve(response);
      })
      .catch(({
        response
      }) => {
        resolve(response);
      });
  });
}

export const TodosUsuarios = () => {
  return new Promise(async resolve => {
    return ApiService.get("usuarios")
      .then((response) => {
        resolve(response.data);
      })
      .catch(({
        response
      }) => {
        resolve(response);
      });
  });
}
