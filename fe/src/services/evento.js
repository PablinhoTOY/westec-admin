import { ApiService } from "./api.config";

export const ObtenerTodosEventos = (gid) => {
  return new Promise(async resolve => {
    return ApiService.get("evento/all/" + gid)
      .then((response) => {
        resolve(response.data);
      })
      .catch(({ response }) => {
        resolve(response);
      });
  });
}

export const GuardarEvento = (evento) => {
  return new Promise(async resolve => {
    return ApiService.post("evento", evento)
      .then((response) => {
        resolve(response);
      })
      .catch(({ response }) => {
        resolve(response);
      });
  });
}

export const BorrarEvento = (eventoId) => {
  return new Promise(async resolve => {
    return ApiService.delete("evento/" + eventoId)
      .then((response) => {
        resolve(response);
      })
      .catch(({ response }) => {
        resolve(response);
      });
  });
}

export const ObtenerEventoAsistencia = (eventoId) => {
  return new Promise(async resolve => {
    return ApiService.get("evento/asistencia/" + eventoId)
      .then((response) => {
        resolve(response.data);
      })
      .catch(({ response }) => {
        resolve(response);
      });
  });
}

export const GuardarAsistencia = (asistencia) => {
  return new Promise(async resolve => {
    return ApiService.post("evento/asistencia", asistencia)
      .then((response) => {
        resolve(response);
      })
      .catch(({ response }) => {
        resolve(response);
      });
  });
}