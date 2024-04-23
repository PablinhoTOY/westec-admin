import { ApiService } from "./api.config";


export const getCountries = async () => {
	return ApiService.get("countries")
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};
export const getStatesofCountry = async (countryIso) => {
	return ApiService.get(`country/${countryIso}`)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};
export const getCitiesbyStateCountry = async (countryIso, stateIso) => {
	return ApiService.get(`country/${countryIso}/state/${stateIso}`)
		.then(response => response.data)
		.catch(response => Promise.resolve(response))
};
