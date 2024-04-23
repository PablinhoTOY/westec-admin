import { ApiService } from "./api.config";

export const ObtenerListadodominio = () => {
  return new Promise(resolve => {
    return ApiService.get("dominios/listaCompleta")
      .then(response => resolve(response.data))
      .catch(response => resolve(response));
  });
}