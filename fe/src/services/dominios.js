import { ApiService } from "./api.config";


export const ObtenerTodosDominios = async () => {
	return ApiService.get("dominios/listaCompleta")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const BuscarDominio = async (data) => {
	return ApiService.post("dominios/buscarDominio", data)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const ObtenerTiposDominios = async () => {
	return ApiService.get("dominios/tipos")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const ObtenerDominiosUsuario = async (data) => {
	return ApiService.post("dominios/usuario", data)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const cotizarDominio = async (data) => {
	return ApiService.post("dominios/cotizar-dominio", data,
		{
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		}
	)
	.then(response => response.data)
	.catch(response => Promise.resolve(response))
}

