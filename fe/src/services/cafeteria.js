import { ApiService } from "./api.config";


export const ObtenerListadoCafeteria = async () => {
	return ApiService.get("cafeteria-lugar/list")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
}

export const guardarCafeteria = async (cafeteria) => {
	return ApiService.post("cafeteria-lugar", cafeteria)
		.then(response => response.data)
		.catch(response => Promise.resolve(response.response))
}

export const borrarCafeteria = async (cafeteria_id) => {
	return ApiService.delete(`cafeteria-lugar/${cafeteria_id}`)
		.then(response => response.data)
		.catch(response => Promise.resolve(response));
}

export const ObtenerOpcionesMenu = async () => {
	return ApiService.get("cafeteria/menu/get/opciones")
		.then(response => response)
		.catch(response => Promise.resolve(response))
}

export const GuardarOpcionesMenu = async (datas) => {
	return ApiService.post("cafeteria/menu/crear/opciones", datas)
		.then(response => response.data)
		.catch(response => Promise.resolve(response.response))
}

export const ObtenerCategoriasOpcionesMenu = async () => {
	return ApiService.get("cafeteria/menu/categorias/opciones")
		.then(response => response)
		.catch(response => Promise.resolve(response))
}

export const GuardarMenu = async (datos) => {
	return ApiService.post("cafeteria/menu/crear", datos, { 'Content-Type': 'multipart/form-data' })
		.then(response => response.data)
		.catch(response => Promise.resolve(response.response))
}

export const ObtenerMenus = async () => {
	return ApiService.get("cafeteria/menus")
		.then(response => response)
		.catch(response => Promise.resolve(response))
}

export const ObtenerMenusDiario = async () => {
	return ApiService.get("cafeteria/menus/day")
		.then(response => response)
		.catch(response => Promise.resolve(response))
}


export const GuardarCategoria = async (datos) => {
	return ApiService.post("cafeteria/menu/crear/categoria", datos)
		.then(response => response.data)
		.catch(response => Promise.resolve(response.response))
}

export const ObtenerListadoCafeteriaV2 = async () => {
	return ApiService.get("cafeteria-lugar/list")
		.then(response => response)
		.catch(response => Promise.resolve(response))
}

export const SaveMenu = async (datos) => {
	return ApiService.post("cafeteria/menu/save", datos)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
}

export const DeleteMenu = async (id, activo) => {
	return ApiService.delete("cafeteria/menu/delete/" + id + 'K' + activo)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
}