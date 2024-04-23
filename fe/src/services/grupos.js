import { ApiService } from "./api.config";

export const ObtenerListadoGrupos = async () => {
	return ApiService.get("grupos/list")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const ObtenerConsumoCafeteriaEstudiante = async (date) => {
	return ApiService.get("cafeteria/consume/" + date)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const GuardarGrupo = async (grupo) => {
	return ApiService.post('grupos', grupo)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const BorrarGrupo = async (grupo_id) => {
	return ApiService.delete(`grupos/${grupo_id}`)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};

export const UsuariosPorGrupo = async (grupo_id) => {
	return ApiService.get(`grupos-usuario/${grupo_id}`)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};