import {
    defineStore
} from "pinia";

import {
    ApiService
} from '../services/api.config.js'

export const useCarritoStore = defineStore('carritoStore', {
    state: () => ({
        dominios: [],
    }),
    actions: {
        async agregarDominio(dominio) {
            return new Promise(resolve => {
                ApiService.get(`costos-tipo/${dominio}`)
                    .then((response) => {
                        const costos = response.data.payload
                        for (let x of costos.costos) {
                            if (x.tipo == 'registro' && x.num_annos == 2) {
                                this.dominios.push({
                                    id: x.id,
                                    dominio: dominio,
                                    tipo: x.tipo,
                                    costo: x.costos_details[0].costo,
                                    descuento: x.costos_details[0].descuento,
                                    years: x.num_annos
                                })
                            }
                        }
                        resolve(response);
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response);
                    });
            });
        },
        async agregarDominioRenovacion(dominio) {
            return new Promise(resolve => {
                ApiService.get(`costos-tipo/${dominio}`)
                    .then((response) => {
                        const costos = response.data.payload
                        for (let x of costos.costos) {
                            if (x.tipo == 'renovacion' && x.num_annos == 1) {
                                this.dominios.push({
                                    id: x.id,
                                    dominio: dominio,
                                    tipo: x.tipo,
                                    costo: x.costos_details[0].costo,
                                    descuento: x.costos_details[0].descuento,
                                    years: x.num_annos
                                })
                            }
                        }
                        resolve(response);
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response);
                    });
            });
        },
        async setDominioPrice(dominio) {
            return new Promise(async resolve => {
                return ApiService.get(`getPrice/${dominio}`)
                    .then((response) => {
                        resolve(response.data);
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response.data);
                    });
            });
        },
        setDataDominio(dominio) {
            let aux = dominio.split('.');
            let tipoDominio = ''
            let canPublic = false;
            let addDoc = false;
            let archivos = null;


            if (aux.length <= 2) {
                tipoDominio = `.${aux[1]}`
            }
            else {
                tipoDominio = `.${aux[1]}.${aux[2]}`
                if (aux[1] == 'ac' || aux[1] == 'sld' || aux[1] == 'edu') {
                    canPublic = true;
                }
                if (aux[1] !== 'com') {
                    addDoc = true
                    archivos = []
                }
            }

            const response = {
                "tipoDominio": tipoDominio,
                "canPublic": canPublic,
                "addDoc": addDoc,
                "archivos": archivos,
            }
            return response
        },
        eliminarDominio(data) {
            this.dominios.forEach((d, index) => {
                if (d.dominio == data.dominio) {
                    this.dominios.splice(index, 1);
                }
            })
            console.log(this.dominios)
        },
        async changeData(dominio) {
            return new Promise(resolve => {
                ApiService.get(`costos-tipo/${dominio.domain}`)
                    .then((response) => {
                        const costos = response.data.payload
                        for (let x of costos.costos) {
                            if (x.tipo == dominio.type && x.num_annos == dominio.years) {
                                dominio.idCatalogDomain = x.id
                                dominio.fullprice = x.costos_details[0].costo
                                dominio.discount = x.costos_details[0].descuento
                                dominio.subTotalCost = dominio.fullprice - x.costos_details[0].descuento
                                for (let y in this.dominios) {
                                    if (this.dominios[y].dominio.includes(dominio.domain)) {
                                        this.dominios[y].id = x.id
                                        this.dominios[y].years = x.num_annos;
                                        this.dominios[y].costo = x.costos_details[0].costo;
                                        this.dominios[y].descuento = x.costos_details[0].descuento;
                                    }
                                }
                            }
                        }
                        resolve(response);
                    })
                    .catch(({
                        response
                    }) => {
                        resolve(response);
                    });
            });
        },
        checkearDominio(data) {
            for (let x in this.dominios) {
                if (this.dominios[x].dominio.includes(data)) {
                    return false
                }
            }
            return true
        },
        limpiarCarrito() {
            this.$reset()
            return 200
        },
    },

    persist: {
        enabled: true,
        strategies: [{
            key: 'carritoKey',
            storage: sessionStorage,
        }]
    },
});

