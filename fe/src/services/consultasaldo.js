import {
  ApiService
} from "./api.config";

export const ConsultarSaldosByToken = (token) => {
  return new Promise(async resolve => {
    return ApiService.get("estudiantes/reportefinal/" + token)
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