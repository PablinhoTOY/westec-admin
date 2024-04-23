// /store/user.js

import {
    defineStore
} from "pinia";

import {
    ApiService
} from '../services/api.config.js'
import Cookies from 'js-cookie'

export const useUserStore = defineStore("user", {
    state: () => ({
        email: null,
        id: null,
        id_acceso: null,
        id_tipo_cliente: null,
        nombre: null,
        apellido: null,
        identificacion: null,
        telefono: null,
        direccion1: null,
        direccion2: null,
        estatus: null,
        id_ubicacion: null,
        estado: null,
        ciudad: null,
        empresa: null,
        cargo: null,
        isAuth: false,
    }),
    getters: {
        authUser: (state) => state.isAuth,
    },
    actions: {
        async login(credenciales) {
            return new Promise(async resolve => {
                return ApiService.post("user/login", credenciales)
                    .then((response) => {
                        const data = response.data.payload;
                        this.email = data.email;
                        this.id = data.id;
                        this.id_acceso = data.id_acceso;
                        this.id_tipo_cliente = data.id_tipo_cliente;
                        this.nombre = data.nombre;
                        this.apellido = data.apellido;
                        this.identificacion = data.identificacion;
                        this.telefono = data.telefono;
                        this.direccion1 = data.direccion1;
                        this.direccion2 = data.direccion2;
                        this.estatus = data.estatus;
                        this.id_ubicacion = data.id_ubicacion;
                        this.estado = data.estado;
                        this.ciudad = data.ciudad;
                        this.empresa = data.empresa;
                        this.cargo = data.cargo;
                        this.isAuth = true
                        resolve(response);
                    })
                    .catch(({
                        response
                    }) => {
                        console.log(response);
                        resolve(response);
                    });
            });
        },
        async reset_password(credenciales, token) {
            return new Promise(async resolve => {
                return ApiService.post('users/resetpassword', {
                    password: credenciales.password,
                    password_confirm : credenciales.password_confirm,
                    token: token
                })
                    .then((response) => {
                        resolve(response)
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response)
                    })
            })
        },
        async reset_request(credenciales) {
            return new Promise(async resolve => {
                return ApiService.post('users/sendmailrecoverpassword', {
                    email: credenciales.email,
                })
                    .then((response) => {
                        resolve(response)
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response)
                    })
            })
        },
        async register(credenciales) {
            return new Promise(async resolve => {
                return ApiService.post("user/register", credenciales)
                    .then((response) => {
                        resolve(response);
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response);
                    });
            });
        },
        async logout() {
            localStorage.removeItem('user')
            Cookies.remove('phd')
            return 200
        },
        checkPerm(permisos, user_permisos) {
            const requiredPermissions = permisos ? permisos : []
            const userPermissions = user_permisos
            return userPermissions.some(permission => requiredPermissions.includes(permission))
        }

    },
    persist: {
        enabled: true,
        strategies: [{
            key: 'user2',
            storage: sessionStorage,
        }]
    },
});