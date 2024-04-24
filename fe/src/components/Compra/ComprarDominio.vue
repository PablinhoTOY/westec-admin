<template>
    <!-- 
  <div class="d-flex flex-column justify-content-center align-center my-6">
    <h2>{{ $t("home.head") }}</h2>
    <p>{{ $t('home.head_subtext') }}</p>
  </div> -->
    <v-fade-transition>
        <div v-show="showAnim" class="my-12 mx-16" style="margin-bottom: 100px !important;">
            <v-btn block class="my-2" @click="imprimircosas()" color="black">imprimicion</v-btn>
            <v-card class="border rounded-b-0 px-5 pt-5 pb-1" elevation="4">
                <h5 class="bold">Carrito de Compras</h5>
                <p class="text-grey">Complete el proceso de compra</p>
            </v-card>


            <v-stepper v-model="step" :items="items" alt-labels show-actions border elevation="16">
                <template v-slot:item.1>
                    <v-card class="d-flex align-center rounded-0" height="75px" :color="colorWestec">
                        <div class="d-flex flex-row align-center justify-content-start p-2 px-6 w-100">
                            <v-icon class="" size="42px">mdi-cart-outline</v-icon>
                            <div class="ml-auto text-right d-flex flex-column gap-1">
                                <h5 class="my-0 bold">Registrar pago</h5>
                                <p class="my-0" style="font-size: 14px;">informacion de pago</p>
                            </div>
                        </div>

                    </v-card>

                    <v-sheet border>


                        <form class="form-inline m-4 my-8 mt-12" onsubmit="return false;">
                            <v-text-field class="v-input-dominio-principal" :label="$t('home.label_search_domain')"
                                variant="outlined" type="text" :loading="domain.loadingDominio" required
                                v-model=domain.buscarDominio.dominio
                                @input="domain.buscarDominio.dominio = domain.buscarDominio.dominio.toLowerCase()"
                                @keydown="handleInput" @paste="handlePaste" :clearable="true">
                                <template #append>
                                    <v-select class="v-select-appended" variant="outlined" density="compact"
                                        :items="domain.domainTypes.tipos"
                                        v-model="domain.buscarDominio.sufijo"></v-select>
                                    <v-btn class="v-btn-dominio rounded-0 rounded-te-lg rounded-be-lg" :color="colorWestec"
                                        size="x-large" type="submit"
                                        @click="validarBuscarDominio(domain.buscarDominio.dominio)"
                                        text="agregar dominio">

                                    </v-btn>
                                </template>
                            </v-text-field>
                            <v-alert v-model="domain.dominioNoValido.status" class="" prominent
                                :color="domain.dominioNoValido.color ? domain.dominioNoValido.color : '#00458d'"
                                :title="domain.dominioNoValido.titulo" border="start" closable
                                :text="domain.dominioNoValido.info" density="compact"
                                :type="domain.dominioNoValido.type ? domain.dominioNoValido.type : null"></v-alert>
                        </form>

                        <v-table class="text-size" hover>
                            <thead>
                                <tr>
                                    <th class="py-5">Descripcion</th>
                                    <th class="">Cantidad</th>
                                    <th class="text-center">Precio por año </th>
                                    <th class="text-end">Descuento</th>
                                    <th class="text-end">Total</th>
                                </tr>
                            </thead>

                            <tbody>
                                <tr v-for="(domain, index) in buyDomains" :key="index">
                                    <td class="">
                                        <div class="py-6 px-2 d-flex flex-row align-center gap-3" style="">
                                            <div class="d-flex align-center justify-content-start ">
                                                <div style="min-width: 170px;">
                                                    <v-btn class="mx-2 mr-5" density="compact" variant="flat"
                                                        icon="mdi-close-circle-outline" color="white"
                                                        @click="borrarCarrito(domain)"></v-btn>
                                                    <v-chip v-if="domain.type == 'registro'" class="mr-6 pb-1"
                                                        variant="flat" density="comfortable" size="large"
                                                        color="success">Registro</v-chip>
                                                    <v-chip v-else-if="domain.type == 'renovacion'" class="mr-6 pb-1"
                                                        variant="flat" density="comfortable" size="large"
                                                        color="info">Renovación</v-chip>
                                                    <v-chip v-else class="mr-6 pb-1" variant="flat"
                                                        density="comfortable" size="large" color="red">Error</v-chip>
                                                </div>


                                            </div>
                                            <div class="d-flex flex-column justify-content-center">
                                                <div class="bold mb-0" style="font-size: 24px;">
                                                    {{ domain.domain }}
                                                </div>
                                                <div class="d-flex flex-column align-center justify-conten-center">
                                                    {{ domain }}
                                                    <div v-for="(servidor, index) in domain.ipServidoresDNS"
                                                        class="d-flex gap-2">
                                                        <v-text-field :key="index" v-model="servidor.nombre"
                                                            @input="sameDomainNameDns(domain.domain, servidor)"
                                                            class="v-server-input my-1" style="width: 200px;"
                                                            variant="outlined"
                                                            :label="`Nombre servidor DNS ${index + 1}`"
                                                            density="compact"></v-text-field>
                                                        <v-text-field v-if="domain.domain == servidor.nombre"
                                                            :key="index" v-model="servidor.ipDNS"
                                                            class="v-server-input my-1" style="width: 200px;"
                                                            variant="outlined" :label="`IP Servidor DNS ${index + 1}`"
                                                            density="compact"></v-text-field>
                                                    </div>


                                                </div>
                                                <div class="d-flex justify-content-center gap-3 mt-2">
                                                    <v-btn @click="domain.ipServidoresDNS.pop()"
                                                        v-if="domain.ipServidoresDNS.length > 1" icon="mdi-minus"
                                                        density="compact" :color="colorWestec"></v-btn>
                                                    <v-btn v-if="domain.ipServidoresDNS.length < 4"
                                                        @click="domain.ipServidoresDNS.push({ nombre: '' })"
                                                        icon="mdi-plus" density="compact" :color="colorWestec"></v-btn>
                                                </div>
                                            </div>

                                            <v-checkbox style="min-width: 115.2px;" v-if="domain.canPublic"
                                                v-model="domain.isPublic" class="ml-4" label="Institucion publica"
                                                :color="colorWestec" @click="descuentoInstitucionPublica(domain)"
                                                hide-details></v-checkbox>

                                        </div>
                                    </td>
                                    <td class="">
                                        <v-select class="v-select-list align-center" rounded="md" density="compact"
                                            suffix="años" :items="domain.type == 'renovacion' ? yearsRenovacion : years"
                                            v-model="domain.years" :key="domain.index" variant="outlined"></v-select>
                                    </td>
                                    <td class="text-end">${{ domain.price.toFixed(2) }}</td>
                                    <td class="text-end">-${{ domain.discount.toFixed(2) }}</td>
                                    <td class="text-end">${{ domain.subTotalCost.toFixed(2) }}</td>
                                </tr>


                                <div class="d-flex gap-3 align-center justify-content-start mx-6 my-2">
                                    <v-card class="d-flex flex-column align-center justify-content-center my-4"
                                        height="75px" width="150px" color="success">
                                        <h4 class="mb-0 bold"> ${{ total.toFixed(2) }}</h4>
                                        <p class="mb-0">Total a pagar</p>
                                    </v-card>

                                    <v-card v-if="true" class="d-flex flex-column align-center justify-content-center"
                                        height="75px" width="150px" color="warning">
                                        <h4 class="mb-0 bold"> ${{ totalDescuento.toFixed(2) }}</h4>
                                        <p class="mb-0 text-center" style="width: 100px; line-height: 16.5px;">Total de
                                            descuento</p>
                                    </v-card>
                                </div>

                            </tbody>

                        </v-table>
                    </v-sheet>
                </template>

                <template v-slot:item.2>
                    <v-card v-if="filteredDomains != 0" class="d-flex align-center rounded-0" height="75px"
                        :color="colorWestec">
                        <div class="d-flex flex-row align-center justify-content-start p-2 px-6 w-100">
                            <v-icon class="" size="42px">mdi-archive</v-icon>
                            <div class="ml-auto text-right d-flex flex-column gap-1">
                                <h5 class="my-0 bold">Subir documentacion</h5>
                                <p class="my-0" style="font-size: 14px;">archivos validantes</p>
                            </div>
                        </div>
                    </v-card>

                    <v-card v-else class="d-flex align-center rounded-0" height="75px" :color="colorWestec">
                        <div class="d-flex flex-row align-center justify-content-start p-2 px-6 w-100">
                            <v-icon class="" size="42px">mdi-credit-card-outline</v-icon>
                            <div class="ml-auto text-right d-flex flex-column gap-1">
                                <h5 class="my-0 bold">Elegir</h5>
                                <p class="my-0" style="font-size: 14px;">metodo de pago</p>
                            </div>
                        </div>
                    </v-card>


                    <v-table v-if="userStore.isAuth && filteredDomains != 0" class="text-size" hover>
                        <tbody>
                            <tr v-for="(domain, index) in filteredDomains" :key="index">
                                <td class="p-5 d-flex gap-2 flex-row align-center justify-content-center"
                                    style="height: 150px;">
                                    <div class="bold" style="font-size: 20px;">
                                        {{ domain.domain }}
                                    </div>
                                    <v-file-input v-model="domain.archivos" class="mt-5" rounded="2"
                                        @change="uploadFile($event, domain)" accept=".pdf,.png,.jpg,.jpeg" counter
                                        label="Adjunte un Archivo [PDF, PNG, JPG, JPEG]" multiple
                                        placeholder="Select your files" prepend-icon="mdi-paperclip" variant="outlined"
                                        :show-size="1000" :clearable="true">
                                        <template v-slot:selection="{ archivos }">
                                            <template v-for="fileName in domain.archivos" :key="fileName">
                                                <v-chip :color="colorWestec" label size="small" class="me-2">
                                                    <v-icon class="mr-1" color="green" size="20"
                                                        v-if="fileName?.type?.includes('image/')">mdi-file-image</v-icon>
                                                    <v-icon class="mr-1" color="red" size="20"
                                                        v-else-if="fileName?.type?.includes('pdf')">mdi-file-pdf-box</v-icon>
                                                    <v-icon class="mr-1" color="grey" size="20" v-else>mdi-file</v-icon>
                                                    {{ fileName.name }} {{ (fileName.size / 1000).toFixed(1) }} kB

                                                </v-chip>
                                            </template>
                                        </template>
                                    </v-file-input>
                                </td>
                            </tr>
                            <div class="my-8">
                                <v-btn block :color="colorWestec" size="large" rounded="lg" type="submit" variant="flat"
                                    :loading='loadingMandarSolicitud' :disabled="isBtnDisabledIraPagar"
                                    @click="sendDocumentacion()">
                                    Cotizar dominio <v-icon class="fa-solid fa-money-check-dollar ml-3"></v-icon>
                                </v-btn>
                            </div>
                            <input type="hidden" :value="isBtnDisabledIraPagar">
                        </tbody>
                    </v-table>

                    <v-sheet v-else-if="userStore.isAuth && filteredDomains == 0" border>
                        <v-card class="gap-3 d-flex flex-column align-center justify-content-center">

                            <v-tabs v-model="tab" class="w-100" height="60" color='#00458d' grow>
                                <v-tab id="pagoEfectivo" value="tab-1" class="text-black">
                                    <v-icon class="mr-4">mdi-credit-card</v-icon>Tarjeta de credito</v-tab>
                                <!-- <v-tab id="pagoTarjeta" value="tab-2" class="text-black">
                                    <v-icon class="mr-4">mdi-cash</v-icon>Efectivo</v-tab> -->
                            </v-tabs>

                            <v-window class="d-flex align-center justify-content-center w-100 windowPagos"
                                v-model="tab">

                                <v-window-item value="tab-1" class="w-100" touchless>
                                    <div class="w-100 d-flex flex-column align-center justify-content-center">
                                        <v-card class="d-flex flex-column align-center justify-content-center 
                                        text-center p-2 pt-5 pb-4 gap-1 mb-5" width="150" height="110" color="success">
                                            <div class="d-flex flex-row align-center gap-1">
                                                <h4 class="mb-0 mt-0 bold" style="font-size: 24px;"> ${{
            total.toFixed(2) }}
                                                </h4>
                                            </div>

                                            <p class="mb-0 mt-0 text-center" style="max-width: 75%; font-size: 11px;">
                                                Total del pago facturado el
                                            </p>
                                            <p class="mb-0 text-white" style="font-size: 14px;">{{ new
            Date().toLocaleDateString() }}</p>
                                        </v-card>

                                        <v-card class="w-50 d-flex justify-content-center" variant="flat"
                                            min-height="200px">


                                            <form method="POST" @submit.prevent="pagarDominiosCredito" class="row">
                                                <div class="my-2 col-12">
                                                    <v-text-field v-model="pagoCredito.namePortador" id="nombreTarjeta"
                                                        label="Nombre portador" rounded="lg" variant="outlined"
                                                        :error-messages="v$.pagoCredito.namePortador.$errors.map(e => e.$message)"
                                                        density="comfortable" prepend-inner-icon="mdi-account"
                                                        @input="pagoCredito.namePortador = pagoCredito.namePortador.toUpperCase()"></v-text-field>
                                                </div>

                                                <div class="my-2 col-12">
                                                    <v-text-field v-model="pagoCredito.creditnumber" id="numeroTarjeta"
                                                        label="Numero de tarjeta" rounded="lg" variant="outlined"
                                                        :error-messages="v$.pagoCredito.creditnumber.$errors.map(e => e.$message)"
                                                        density="comfortable"
                                                        prepend-inner-icon="mdi-credit-card-outline"
                                                        v-mask="'#### #### #### ####'"></v-text-field>
                                                </div>


                                                <div class="my-2 col-md-6 col-6">
                                                    <v-text-field v-model="pagoCredito.ccexp" id="ccexp"
                                                        label="Expiracion" rounded="lg" variant="outlined"
                                                        density="comfortable" hint="MM/YY Ej: 04/25"
                                                        :error-messages="v$.pagoCredito.ccexp.$errors.map(e => e.$message)"
                                                        persistent-hint prepend-inner-icon="mdi-calendar-range"
                                                        v-mask="expMask"></v-text-field>
                                                </div>

                                                <div class="my-2 col-md-6 col-6">
                                                    <v-text-field v-model="pagoCredito.cvv" id="cvv" label="CVV"
                                                        rounded="lg" variant="outlined" density="comfortable"
                                                        prepend-inner-icon="mdi-num"
                                                        :error-messages="v$.pagoCredito.cvv.$errors.map(e => e.$message)"
                                                        v-mask="'####'" type="tel">
                                                        <template #append-inner>
                                                            <v-menu open-on-hover offset-y
                                                                :close-on-content-click="false"
                                                                transition="slide-y-transition" location="bottom"
                                                                open-delay="0" close-delay="0">
                                                                <template #activator="{ props }">
                                                                    <v-icon v-bind="props" style="cursor: help;">
                                                                        mdi-help-circle-outline
                                                                    </v-icon>
                                                                </template>
                                                                <v-card>
                                                                    <v-list>
                                                                        <v-list-item>
                                                                            <img src="../../static/img/cvvExplain.jpg"
                                                                                width="400" alt="CVV">
                                                                        </v-list-item>
                                                                    </v-list>
                                                                </v-card>
                                                            </v-menu>
                                                        </template>
                                                    </v-text-field>
                                                </div>

                                                <div class="my-8">
                                                    <v-btn block :color="colorWestec" size="large" rounded="lg"
                                                        type="submit" variant="flat" :loading='loadingPagando'>
                                                        Pagar <v-icon
                                                            class="fa-solid fa-money-check-dollar ml-3"></v-icon>
                                                    </v-btn>
                                                </div>



                                            </form>

                                        </v-card>
                                    </div>


                                </v-window-item>

                                <!-- <v-window-item value="tab-2" touchless>
                                    <v-card class="d-flex flex-column align-center justify-content-center text-center"
                                        height="300px" min-width="300px" max-width="600px" variant="flat">
                                        <h4 class="text-h5">{{ `Si desea pagar en efectivo tiene un plazo de
                                            5 dias para pagar, si no paga en el plazo de estos dias se eliminara la
                                            peticion completamente.` }}</h4>

                                        <v-card width="100%">
                                            <v-btn class="mt-5" id="loginId" :color="colorWestec" rounded="lg"
                                                variant="elevated" elevation="8" height="50px" block
                                                append-icon="mdi-send" to="">
                                                mandar peticion
                                            </v-btn>
                                        </v-card>

                                    </v-card>
                                </v-window-item> -->

                            </v-window>
                            <!-- <div class="w-50 my-2">
                                <div id="paypalButton"></div>
                                <div class="col d-flex align-center justify-content-center gap-3">
                                    <div class="col d-flex align-center justify-content-center gap-3">
                                        <v-btn class="v-btn-dominio rounded-2" :color="colorWestec" size="x-large" type="submit"
                                            @click="">
                                            mastercard <v-icon class="fa-brands fa-cc-mastercard ml-2" size="40px"></v-icon>
                                        </v-btn>
                                        <v-btn class="v-btn-dominio rounded-2" :color="colorWestec" size="x-large" type="submit"
                                            @click="">
                                            Visazo <v-icon class="fa-brands fa-cc-visa ml-2" size="40px"></v-icon>
                                        </v-btn>
                                    </div>
                                </div>
                            </div> -->

                        </v-card>
                    </v-sheet>

                    <v-sheet class="d-flex flex-column align-center justify-content-center" v-else border>
                        <v-card class="d-flex flex-column align-center justify-content-center text-center"
                            height="300px" min-width="300px" max-width="600px" variant="flat">
                            <h4 class="">Para proseguir necesita
                                <span class="bold">iniciar sesion</span>
                            </h4>
                            <div class="d-flex flex-row align-center justify-content-center gap-5">

                                <v-icon :color="colorWestec" size="85px">mdi-account-key</v-icon>
                                <v-btn class="" id="loginId" :color="colorWestec" variant="elevated" elevation="8"
                                    height="50px" width="150px" text="Login" prepend-icon="mdi-login-variant"
                                    to="">

                                </v-btn>
                            </div>
                        </v-card>
                    </v-sheet>



                    <!-- <v-card v-else class="d-flex flex-column align-center justify-content-center text-center"
                            height="300px" variant="flat">
                            <h4 class="bold">Dominio(s) no requieren de documentacion adicional</h4>
                            <h5 class="bold">puede saltarse este paso</h5>
                            <v-icon :color="colorWestec" size="100px">mdi-arrow-right-thick</v-icon>
                        </v-card> -->


                </template>
            </v-stepper>

        </div>
    </v-fade-transition>
</template>

<style>
/* estilos personalizados para 
componentes de vuetify dentro de
este componente Vue*/

.v-stepper-item__content {
    color: black;
}

.v-stepper-actions {
    .v-btn {
        color: black !important;
    }
}

.text-size {
    font-size: 16px !important;
}

.v-server-input {
    .v-label {
        font-size: 13px !important;
    }

    .v-input__details {
        display: none;
    }
}

.v-select-list {
    width: 125px;

    .v-field__input {
        font-size: 16px !important;
    }

    .v-input__details {
        display: none;
    }
}

.v-select-list {
    width: 125px;

    .v-field__input {
        font-size: 16px !important;
    }

    .v-input__details {
        display: none;
    }
}

.iconsContainer {
    width: 32px !important;
    height: 32px !important;
}

.icons {
    width: 24px !important;
    height: 24px !important;
}

.windowPagos {
    padding-top: 40px;
    padding-bottom: 40px;

    .v-window__container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
}
</style>

<script>

import * as dominiosService from '../../services/dominios.js'
import * as facturacionService from '../../services/facturacion.js'
import { watchEffect } from 'vue'
import * as msg from '../../helpers/mensajes'
import useValidate from '@vuelidate/core'
import { required, helpers, minLength, numeric } from '@vuelidate/validators'
import { useCarritoStore } from '../../stores/carrito'
import { useUserStore } from '../../stores/user'
import { mask } from 'vue-the-mask'
import CryptoJS from 'crypto-js';

//import { loadScript } from "@paypal/paypal-js";
import Swal from 'sweetalert2'

export default {
    setup() {
        const carritoStore = useCarritoStore();
        return { carritoStore, userStore }
    },
    directives: {
        mask
    },
    data() {
        return {
            v$: useValidate(),
            dominio: '',
            fileSizeError: false,
            showAnim: false,
            shipping: 0,
            step: 1,
            loadingPagando: false,
            loadingMandarSolicitud: false,
            loadingDominio: false,
            //paypalLoaded: false,
            tab: 'tab-1',
            pagoCredito: {
                namePortador: '',
                creditnumber: '',
                ccexp: '',
                cvv: '',
            },
            items: [
                'Carrito',
                'Procesos'
            ],
            listaCostos: [],
            buyDomains: [],
            oldBuyDomains: [], // Added to store the previous state
            deleteDomainCarrito: [],
            specialDomains: [],
            //años para registro
            years: [
                2, 3, 4, 5,
            ],
            //años para renovacion
            yearsRenovacion: [
                1, 2, 3, 4,
            ],
            domain: {
                buscarDominio: {
                    dominio: '',
                    sufijo: '.pa',
                    dominioCompleto: '',
                },
                resBuscarDominio: [],
                dominioNoValido: {
                    titulo: '',
                    info: '',
                    type: '',
                    color: '',
                    status: false,
                },
                domainTypes: {
                    response: [],
                    tipos: [],
                }
            },

            //mascara especial para la fecha de expiracion de la tarjeta de credito
            expMask: {
                mask: 'FG/##',
                tokens: {
                    'F': {
                        pattern: /[0-1]/,
                    },
                    'G': {
                        pattern: /[0-9]/,
                    },
                    '#': { pattern: /\d/ }
                }
            },
        };
    },
    watch: {
        buyDomains: {
            handler: function (newVal) {
                newVal.forEach((item, index) => {
                    if (item.years !== this.oldBuyDomains[index]?.years) {
                        this.carritoStore.changeData(this.buyDomains[index]);
                    }
                });
                // Update oldBuyDomains with the new value for next comparison
                this.oldBuyDomains = JSON.parse(JSON.stringify(newVal));
            },
            deep: true,
            immediate: true // Trigger on initial mount
        }
    },
    validations() {
        return {
            pagoCredito: {
                namePortador: {
                    required: helpers.withMessage('Valor requerido', required),
                    validName: helpers.withMessage(
                        () => 'El nombre no puede contener numeros ni caracteres especiales',
                        (value) => /^[a-zA-Zñ ]+$/.test(value))
                },
                creditnumber: {
                    required: helpers.withMessage('Valor requerido', required),
                    minLength: helpers.withMessage('Introduzca un formato de tarjeta de credito valida', minLength(19)),
                },
                ccexp: {
                    required: helpers.withMessage('Valor requerido', required),
                    minLength: helpers.withMessage('Fecha de expiracion incompleta', minLength(5)),
                },
                cvv: {
                    required: helpers.withMessage('Valor requerido', required),
                    minLength: helpers.withMessage('El CVV requiere un minimo de tres digitos', minLength(3)),
                },
            }
        }
    },
    computed: {
        total() {
            return this.buyDomains.reduce((acc, domain) => acc + domain.fullprice - domain.discount, 0)
        },
        totalDescuento() {
            return this.buyDomains.reduce((acc, domain) => acc + domain.discount, 0)
        },

        //filtra los dominios que necesitan documentacion
        filteredDomains() {
            let filtered = this.buyDomains.filter(domain => domain.archivos != null);
            return filtered;
        },
        isBtnDisabledIpServers() {
            if (this.buyDomains.every(domain => domain.ipServidoresDNS.every(ipsDNS => ipsDNS.ipDNS != '' && ipsDNS.nombre != ''))) {
                document.querySelector('.v-stepper-actions .v-btn--variant-tonal').removeAttribute('disabled')
                document.querySelector('.v-stepper-actions .v-btn--variant-tonal').classList.remove('v-btn--disabled')
                return false;
            } else {
                //revisa si la pagina es el 1 donde esta la validacion, si es asi la bloquea hasta que cada archivo 
                //sea agregado para todos los dominios que lo necesiten
                if (this.step == 1) {
                    return true;
                }
            }
        },
        isBtnDisabledIraPagar() {
            // Método para verificar si el botón de ir a pagar está deshabilitado
            // el querySelector('.v-stepper-actions .v-btn--variant-tonal') es porque no se puede modificar el boton del 
            // stepper de vuetify directamente
            if (this.filteredDomains.every(domain => domain.archivos.length > 0)) {
                return false;
            } else {
                if (this.step == 2) {
                    return true;
                }
            }
        },
    },
    methods: {
        async setDataDominios() {
            this.buyDomains = []
            for (let x in this.carritoStore.dominios) {
                let dominio = this.carritoStore.dominios[x].dominio;
                let tipo = this.carritoStore.dominios[x].tipo;
                let ipServidoresDNS = [{
                    nombre: '',
                }]

                let price = (this.carritoStore.dominios[x].costo / this.carritoStore.dominios[x].years)
                const subData = this.carritoStore.setDataDominio(dominio)

                let annos = this.carritoStore.dominios[x].years;
                let fullprice = this.carritoStore.dominios[x].costo;
                let discount = this.carritoStore.dominios[x].descuento;

                this.buyDomains.push({
                    index: x,
                    idCatalogDomain: this.carritoStore.dominios[x].id,
                    domain: dominio,
                    domainType: subData.tipoDominio,
                    ipServidoresDNS: ipServidoresDNS,
                    type: tipo,
                    years: annos,
                    price: price,
                    fullprice: fullprice,
                    discount: discount,
                    subTotalCost: (fullprice - discount),
                    canPublic: subData.canPublic,
                    isPublic: subData.isPublic,
                    addDoc: subData.addDoc,
                    archivos: subData.archivos ? subData.archivos : null,
                })
            }
        },
        //descuenta totalmente todo el costo de los archivos porque estos son gratuitos
        async descuentoInstitucionPublica(domain) {
            domain.isPublic = !domain.isPublic;
            if (domain.isPublic) {
                domain.discount = (domain.price * domain.years);
                domain.subTotalCost = 0
            }
            else {
                await this.setDataDominios();
            }
        },

        uploadFile(event, domain) {
            domain.archivos = [];
            this.fileSizeError = false; // Restablecer el error al seleccionar nuevos archivos
            for (let i = 0; i < event.target.files.length; i++) {
                //const file = this.$refs.fileInput[index].files[i]
                const file = event.target.files[i]
                if (file.size / (1024 * 1024) > 14) {

                    this.fileSizeError = true; // Restablecer el error al seleccionar nuevos archivos
                    event.target.files = []

                    break;
                }
                domain.archivos.push(file);
            }
        },

        // pagarconPaypal() {
        //     loadScript({ clientId: "test", currency: "USD" })
        //         .then((paypal) => {
        //             paypal
        //                 .Buttons({
        //                     style: {
        //                         layout: 'vertical',
        //                         color: 'gold',
        //                         shape: 'rect',
        //                         label: 'paypal',
        //                         disableMaxWidth: true,
        //                     },
        //                     createOrder: this.createOrder,
        //                     onApprove: this.onApprove,
        //                 })
        //                 .render('#paypalButton')
        //                 .catch((error) => {
        //                     console.error("failed to render the PayPal Buttons", error);
        //                 });
        //         })
        //         .catch((error) => {
        //             console.error("failed to load the PayPal JS SDK script", error);
        //         });
        // },
        // createOrder(data, actions) {
        //     console.log('Creating order...')
        //     return actions.order.create({
        //         purchase_units: [{
        //             amount: {
        //                 value: this.total,
        //             },
        //         },],
        //     })
        // },
        // onApprove(data, actions) {
        //     console.log('Order approved...')
        //     return actions.order.capture().then(() => {
        //         msg.toastr(`LISTO PA ya pagaste tu deuda de $${this.total}`, 'success')
        //         console.log('Order complete!')
        //     })
        // },


        clearArchivos(domain) {
            domain.archivos = [];
            console.log(domain)
        },

        getCostos() {
            facturacionService
                .getCostos()
                .then((response) => {
                    this.listaCostos = response.payload
                })
                .catch((err) => console.log(err))
        },

        getDomainTypes() {
            dominiosService
                .ObtenerTiposDominios()
                .then((response) => {
                    this.domain.domainTypes.response = response
                    for (let tipo of this.domain.domainTypes.response) {
                        this.domain.domainTypes.tipos.push(tipo.nombre)
                    }
                })
                .catch((err) => console.log(err))
        },

        validarBuscarDominio(value) {
            //revisa si - esta al principio o al final del value,
            // y con los caracteres que son los validos
            const allowedCharactersRegex = /^(?!-)(?!.*-$)[a-zA-Z0-9ñ-]+$/;
            if (value != '' && value != null) {
                if (allowedCharactersRegex.test(value)) {
                    this.getDominio();
                } else {
                    this.domain.dominioNoValido.titulo = 'Caracteres especiales invalidos';
                    this.domain.dominioNoValido.info = 'solo se permiten caracteres alfanumericos y el caracter "-" en medio del dominio.';
                    this.domain.dominioNoValido.type = 'info'
                    this.domain.dominioNoValido.color = '#00458d'
                    this.domain.dominioNoValido.status = true;
                }
            }
            else {
                this.domain.dominioNoValido.titulo = 'Campo vacio';
                this.domain.dominioNoValido.info = 'Se requiere que ingrese un dominio.';
                this.domain.dominioNoValido.type = 'info'
                this.domain.dominioNoValido.color = '#00458d'
                this.domain.dominioNoValido.status = true;
            }
        },

        sameDomainNameDns(dominio, servidor) {
            if (dominio == servidor.nombre) {
                servidor.ipDNS = ''
            } else {
                delete servidor.ipDNS
            }
        },

        async getDominio() {
            this.domain.loadingDominio = true
            this.domain.buscarDominio.dominioCompleto = this.domain.buscarDominio.dominio + this.domain.buscarDominio.sufijo
            await dominiosService
                .BuscarDominio(this.domain.buscarDominio)
                .then((async (response) => {
                    if (response.status == 200) {
                        for (let x of response.payload) {
                            if (x.principal) {
                                if (!x.existe) {
                                    if (this.carritoStore.checkearDominio(x.dominioBuscado)) {
                                        await this.carritoStore.agregarDominio(x.dominioBuscado)
                                        msg.toastrTimeLong(`Dominio ${x.dominioBuscado} agregado`, 'success')
                                        this.domain.dominioNoValido.status = false;
                                        await this.setDataDominios();
                                    }
                                    else {
                                        this.domain.dominioNoValido.titulo = `Dominio duplicado: ${x.dominioBuscado}`;
                                        this.domain.dominioNoValido.info = 'No se puede agregar el mismo dominio dos veces.';
                                        this.domain.dominioNoValido.type = 'warning'
                                        this.domain.dominioNoValido.color = 'warning'
                                        this.domain.dominioNoValido.status = true;
                                    }
                                }
                                else {
                                    this.domain.dominioNoValido.titulo = `Dominio ya existente: ${x.dominioBuscado}`;
                                    this.domain.dominioNoValido.info = `El dominio ${x.dominioBuscado} ya existe si desea renovar, inicie sesion.`;
                                    this.domain.dominioNoValido.type = 'error'
                                    this.domain.dominioNoValido.color = '#d12229'
                                    this.domain.dominioNoValido.status = true;
                                }
                            }
                        }
                        this.domain.loadingDominio = false
                    }
                    else {
                        msg.ShowMessages(data)
                        this.domain.loadingDominio = false
                    }
                }))
                .catch((err) => console.log(err), this.domain.loadingDominio = false)
        },

        handleInput(event) {
            //
            const allowedCharactersRegex = /^[a-zA-Z0-9ñ-]+$/;
            if (!allowedCharactersRegex.test(event.key)) {
                event.preventDefault();
            }
            else if (event.altKey) {
                event.preventDefault();
            }
        },

        handlePaste(event) {
            const allowedCharactersRegex = /^[a-zA-Z0-9ñ-]+$/;
            // Get the pasted text from the clipboard
            const pastedText = (event.clipboardData || window.clipboardData).getData('text');

            // Check if the pasted text contains only allowed characters
            if (!allowedCharactersRegex.test(pastedText)) {
                event.preventDefault();
                this.domain.dominioNoValido.titulo = 'Paste invalido';
                this.domain.dominioNoValido.info = 'Su ultimo texto de portapapeles tiene caracteres invalidos.';
                this.domain.dominioNoValido.type = 'warning'
                this.domain.dominioNoValido.color = '#00458d'
                this.domain.dominioNoValido.status = true;
            }
        },
        async borrarCarrito(data) {
            Swal.fire({
                title: 'Eliminar dominio',
                text: `Está seguro de que desea eliminar el dominio ${data.domain}?`,
                showDenyButton: true,
                confirmButtonText: 'Eliminar',
                confirmButtonColor: '#00458d',
                denyButtonText: 'Cerrar',
            }).then(async (result) => {
                if (result.isConfirmed) {
                    this.deleteDomainCarrito = {
                        dominio: data.domain,
                        tipo: data.type,
                    }
                    this.carritoStore.eliminarDominio(this.deleteDomainCarrito)
                    msg.toastrTime('Eliminado', 'success')
                    await this.setDataDominios();
                }
            }).catch((err) => console.log(err))
        },

        fileToBase64(file) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = () => resolve(reader.result.split(',')[1]);
                reader.onerror = error => reject(error);
            });
        },

        deepCloneArrayWithFiles(array) {
            return array.map(item => {
                let newItem = Object.assign({}, item);  // Shallow copy of the item object
                if (item.archivos && Array.isArray(item.archivos)) {
                    newItem.archivos = item.archivos.map(file => {
                        // Assuming `file` is a File object, we directly assign it
                        // If `file` is more complex or a nested object, further cloning logic might be required
                        return new File([file], file.name, {
                            type: file.type,
                            lastModified: file.lastModified,
                        });
                    });
                }
                return newItem;
            });
        },

        async sendDocumentacion() {
            this.loadingMandarSolicitud = true;

            let formData = new FormData();

            const dominios = this.deepCloneArrayWithFiles(this.buyDomains);
            for (let e of dominios) {
                for (let a in e.archivos) {
                    formData.append('files', e.archivos[a])
                    e.archivos[a] = e.archivos[a]['name'];
                }
            }

            formData.append('dominios', JSON.stringify(dominios))
            formData.append('userdata', JSON.stringify({
                "nombre": this.userStore.nombre,
                "apellido": this.userStore.apellido,
                "empresa": this.userStore.empresa,
                "id_ubicacion": this.userStore.id_ubicacion,
                "estado": this.userStore.estado,
                "ciudad": this.userStore.ciudad,
                "telefono": this.userStore.telefono,
                "forma_pago": 'tarjeta_credito',
                "acceso": this.userStore.id_acceso,
                "email": this.userStore.email,
            }))

            console.log([...formData])
            this.loadingMandarSolicitud = false;
            dominiosService.cotizarDominio(formData)
                .then((response) => {
                    console.log(response)
                    if (response.status == 200) {
                        //logica si salio bien todo
                        msg.toastr('Solicitud enviada', 'Se ha enviado la solicitud de documentacion', 'success')
                        // this.carritoStore.limpiarCarrito()
                        // this.step = 1;
                        // await this.setDataDominios()
                        // this.$router.push()
                    }
                    else {
                        msg.ShowMessages(response)
                    }
                    this.loadingMandarSolicitud = false;
                })
                .catch((err) => console.log(err))
        },

        async pagarDominiosCredito() {
            this.v$.$touch()

            
            if (!this.v$.$error) {
                this.loadingPagando = true;
                try {
                    //le quitamos los caracteres especiales de las mascaras
                    let ccnumber = this.pagoCredito.creditnumber.replaceAll(' ', '')
                    let ccexp = this.pagoCredito.ccexp.replace('/', '')
                    let dominios_format;
                    let clientIp;

                    await fetch('https://api.ipify.org?format=json')
                        .then(x => x.json())
                        .then(x => {
                            clientIp = x.ip
                        });

                    dominios_format = this.formatDescripcionDominios();

                    const dominios = JSON.parse(JSON.stringify(this.buyDomains));
                    
                    const order = { orderdescription: `Venta de dominio(s): ${dominios_format}`, ipaddress: clientIp};

                    //datos provenientes del info del usuario logueado
                    const billing = {
                        firstname: this.userStore.nombre,
                        lastname: this.userStore.apellido,
                        company: this.userStore.empresa,
                        address1: this.userStore.direccion1,
                        ...(this.userStore.direccion2 ? { address2: this.userStore.direccion2 } : {}),
                        country: this.userStore.id_ubicacion,
                        ...(this.userStore.estado ? { state: this.userStore.estado } : {}),
                        ...(this.userStore.ciudad ? { city: this.userStore.ciudad } : {}),
                        phone: this.userStore.telefono,
                        email: this.userStore.email,
                        id_acceso: this.userStore.id_acceso,
                    };

                    //datos cc
                    const datos = {
                        ccnumber: ccnumber,
                        ccexp: ccexp,
                        amount: this.total.toFixed(2),
                        cvv: this.pagoCredito.cvv,
                    };

                    //bloque de datos
                    const blockDatos = {
                        dominios: dominios,
                        order: order,
                        billing: billing,
                        datos: datos,
                    }

                    //encripta la llave unica base64
                    const derived_key = CryptoJS.enc.Base64.parse(import.meta.env.VITE_ENCRYPT_SALT);

                    const encryptionOptions = {
                        //numero de 16 digitos Initialization vector (IV)
                        iv: CryptoJS.enc.Utf8.parse(import.meta.env.VITE_IV),
                        mode: CryptoJS.mode.CBC,
                    };

                    //encryptacion de los datos y se mandan al backend
                    let jsonData = CryptoJS.AES.encrypt(JSON.stringify(blockDatos), derived_key, encryptionOptions).toString()

                    //adaptando el string en un json
                    jsonData = {
                        data: jsonData
                    }

                    await facturacionService
                        .pagoCredito(jsonData)
                        .then(async (response) => {
                            console.log(response)
                            if (response.status == 200) {
                                msg.toastr('Compra exitosa', `La compra de los dominios ${this.formatDescripcionDominios()} por el total de $${this.total} ha sido procesada`, 'success')
                                //this.carritoStore.limpiarCarrito()
                                await this.setDataDominios()
                            }
                            else {
                                msg.ShowMessages(response)
                            }
                            this.loadingPagando = false;
                        }
                        ).catch((err) => console.log(err))

                } catch (error) {
                    console.error('Error:', error);
                }
            }
        },
        formatDescripcionDominios() {
            let dominios; // Variable para almacenar la descripción de los dominios
            for (let x of this.buyDomains) {
                // Verifica si es el segundo elemento de una lista de dos elementos
                if (x.index != 0 && x.index == 1 && this.buyDomains.length == 2) {
                    dominios += `, ${x.domain}` // Agrega el dominio con coma al inicio
                }
                // Verifica si es el segundo elemento
                else if (x.index != 0 && x.index == 1) {
                    dominios += `, ${x.domain}, ` // Agrega el dominio con comas al inicio y al final
                }
                // Verifica si es el último elemento
                else if (x.index != 0 && x.index == this.buyDomains.length - 1) {
                    dominios += `${x.domain}`
                }
                // Verifica si no es el primer elemento
                else if (x.index != 0) {
                    dominios += `${x.domain}, `
                }
                // Si es el primer elemento 
                else {
                    dominios = `${x.domain}` // Inicializa la variable con el primer dominio
                }
            }
            return dominios
        },
        imprimircosas() {
            // console.log(this.pagoCredito)
            // console.log(this.pagoCredito.creditnumber.replaceAll(' ', ''))
            // console.log(this.formatDescripcionDominios())
            console.log(this.buyDomains)
            //console.log(this.listaCostos)
            // for (let x of this.buyDomains) {

            //     for (let b of this.listaCostos) {
            //         if (b.costos_details[0].costo == x.fullprice && b.dominio_tipo.nombre == x.domainType
            //             && b.num_annos == x.years && b.tipo == x.type) {
            //             console.log(b)
            //         }
            //     }
            //     console.log(x)
            // }
        },
        inicializaciones() {

            // Oculta el elemento con el id 'carritoId'
            document.getElementById('carritoId').classList.add('d-none');

            this.showAnim = true;

            // Establece texto para los botones del stepper
            document.querySelector('.v-stepper-actions .v-btn--variant-text .v-btn__content').innerHTML = 'Previo';
            document.querySelector('.v-stepper-actions .v-btn--variant-tonal .v-btn__content').innerHTML = 'Siguente';

            const iconazos = [
                {
                    icon: 'mdi-lead-pencil',
                    //color: 'bg-info',
                },
                {
                    icon: 'mdi-file-document-multiple-outline',
                    // color: 'bg-success',
                },
            ]
            for (let x = 0; x < 2; x++) {
                let item = document.getElementsByClassName('v-stepper-item__avatar')[x]; // Obtiene el elemento con la clase 'v-stepper-item__avatar'
                item.innerHTML = ''; // Limpia el contenido del elemento
                item.classList.add('iconsContainer'); // Agrega la clase 'iconsContainer' al elemento
                item.style.background = this.colorWestec; // Establece el color de fondo del elemento
                let icon = document.createElement('i'); // Crea un elemento de tipo 'i' para el icono
                icon.classList.add(iconazos[x].icon); // Agrega las clases al icono
                icon.classList.add('mdi');
                icon.classList.add('v-icon');
                icon.classList.add('icons');
                item.appendChild(icon); // Agrega el icono al elemento
            }

            watchEffect(() => {
                if (this.step == 1) {
                    if (this.buyDomains.length > 0) {
                        console.log(this.isBtnDisabledIpServers)
                        if (this.isBtnDisabledIpServers) {
                            document.querySelector('.v-stepper-actions .v-btn--variant-tonal').classList.add('v-btn--disabled')
                            document.querySelector('.v-stepper-actions .v-btn--variant-tonal').setAttribute('disabled', true)
                        }
                    } else {
                        document.querySelector('.v-stepper-actions .v-btn--variant-tonal').classList.add('v-btn--disabled')
                        document.querySelector('.v-stepper-actions .v-btn--variant-tonal').setAttribute('disabled', true)
                    }

                }
                if (this.step == 2) {
                    // solo si hay dominios que necesitan documentacion se tirara el codigo
                    if (this.filteredDomains != 0) {
                        if (this.isBtnDisabledIraPagar) {
                            document.querySelector('.v-stepper-actions .v-btn--variant-tonal').classList.add('v-btn--disabled')
                            document.querySelector('.v-stepper-actions .v-btn--variant-tonal').setAttribute('disabled', this.isBtnDisabledIraPagar)
                        }
                    }
                }
            }
            )

        },
    },
    async mounted() {
        this.getDomainTypes();
        this.getCostos();
        await this.setDataDominios();
        this.inicializaciones();

    },
}

</script>