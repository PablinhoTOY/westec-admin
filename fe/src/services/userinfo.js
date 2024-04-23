import { ApiService } from "./api.config";


export const getuserContacts = async (data) => {
	return ApiService.post("userinfo/contactos", data)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const getTiposAreasEmpresas = async () => {
	return ApiService.get("userinfo/areasempresas")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const getUbicaciones = async () => {
	return ApiService.get("userinfo/ubicaciones")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};
export const getUbicacion = async (locale, id) => {
	return ApiService.get(`userinfo/ubicacion/${locale}/${id}`)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const getTipoIdentificaciones = async () => {
	return ApiService.get("userinfo/identificadores")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};
