<template>
    <!-- 
  <div class="d-flex flex-column justify-content-center align-center my-6">
    <h2>{{ $t("home.head") }}</h2>
    <p>{{ $t('home.head_subtext') }}</p>
  </div> -->

    <v-fade-transition>
        <div v-show="showAnim" v-if="!loading" class="my-12 mx-16">
            <div class="mb-6 d-flex flex-column align-center justify-content-center border rounded-lg elevation-16">
                <div class="w-100">
                    <v-card class="border-bottom rounded-b-0 px-5 pt-5 pb-1 rounded-lg" :color="colorWestec">
                        <h5 class="bold">Perfil</h5>
                        <p class="">Informacion de su perfil</p>
                    </v-card>
                </div>
                <div class="p-2 p-lg-4 p-xl-5">
                    <form action="" class="row">
                        <div class="my-2 col-xl-4 col-md-6 col-12">
                            <v-text-field id="nombres" v-model="usuario.nombre" label="Nombre" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-account"></v-text-field>
                        </div>
                        <div class="my-2 col-xl-4 col-md-6 col-12">
                            <v-text-field id="apellido" v-model="usuario.apellido" label="Apellido" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-account"></v-text-field>
                        </div>
                        <div class="my-2 col-xl-4 col-md-6 col-12">
                            <v-text-field id="identificacion" v-model="usuario.identificacion" label="Identificacion"
                                :readonly="readOnly" rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-card-account-details"></v-text-field>
                        </div>

                        <div class="my-2 col-xl-4 col-md-6 col-12">
                            <v-text-field id="Pais" v-model="usuario.pais" label="Pais" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-earth"></v-text-field>
                        </div>
                        <div class="my-2 col-xl-4 col-md-6 col-12">
                            <v-text-field id="Estado" v-model="usuario.estado" label="Estado" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-account"></v-text-field>
                        </div>
                        <div class="my-2 col-xl-4 col-md-6 col-12">
                            <v-text-field id="Ciudad" v-model="usuario.ciudad" label="Ciudad" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-city-variant"></v-text-field>
                        </div>

                        <div class="my-2 col-md-6 col-12">
                            <v-text-field id="CorreoElectronico" v-model="usuario.email" label="Correo Electronico"
                                :readonly="readOnly" rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-email"></v-text-field>
                        </div>

                        <div class="my-2 col-md-6 col-12">
                            <v-text-field id="Telefono" v-model="usuario.telefono" label="Telefono" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-phone"></v-text-field>
                        </div>

                        <div class="my-2 col-md-6 col-12">
                            <v-text-field id="Direccion1" v-model="usuario.direccion1" label="Direccion 1"
                                :readonly="readOnly" rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-sign-direction"></v-text-field>
                        </div>
                        <div class="my-2 col-md-6 col-12">
                            <v-text-field id="Direccion2" v-model="usuario.direccion2" label="Direccion 2"
                                :readonly="readOnly" rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-sign-direction"></v-text-field>
                        </div>
                        <div class="my-2 col-xl-3 col-6">
                            <v-text-field id="Empresa" v-model="usuario.empresa" label="Empresa" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-domain"></v-text-field>
                        </div>
                        <div class="my-2 col-xl-3 col-6">
                            <v-text-field id="Cargo" v-model="usuario.cargo" label="Cargo" :readonly="readOnly"
                                rounded="lg" variant="outlined" density="comfortable"
                                prepend-inner-icon="mdi-briefcase"></v-text-field>
                        </div>
                        <div class="my-2 col-6">
                            <!-- <v-btn block :color="readOnly ? colorWestec : 'warning'" size="large" rounded="lg"
                                variant="elevated" @click="editProfile()">
                                {{ readOnly ? 'Editar' : 'Dejar de editar' }}
                            </v-btn> -->
                        </div>
                    </form>
                </div>
            </div>


            <v-data-table v-if="contactosUsuario != undefined" :headers="headers" :items="contactosUsuario"
                :search="search" :items-per-page="10" class="border rounded-lg elevation-16">
                <template #top>
                    <v-card class="border-bottom rounded-b-0 px-5 pt-5 pb-1 mb-3 rounded-lg" :color="colorWestec">
                        <h5 class="bold">Contactos</h5>
                        <p class="">Contactos de sus dominios</p>
                    </v-card>
                    <v-text-field v-model="search" label="Escriba aquí para filtrar los datos (cualquier columna)..."
                        class="mx-4" prepend-inner-icon="mdi-magnify" rounded="lg"></v-text-field>
                </template>
                <template #item.contactos_dominios="{ item }">
                    <v-dialog width="auto" eager>
                        <template v-slot:activator="{ props: activatorProps }">
                            <v-btn v-bind="activatorProps" class="mr-2" text="Ver" flat density="comfortable"
                                :color="colorWestec" @click="console.log(item.contactos_dominios)">
                                <template #append>
                                    <v-icon>mdi-eye-outline</v-icon>
                                </template>
                            </v-btn>
                        </template>
                        <template v-slot:default="{ isActive }">
                            <v-card prepend-icon="mdi-contacts" class="p-4" rounded="lg"
                                text="Se muestran los dominios a los que esta relacionado este contacto."
                                :title="`Dominios del contacto: ${item.nombre}`">
                                <v-data-table :headers="headersDominioContacto" :items="item.contactos_dominios"
                                    :items-per-page="10" class="mt-2" variant="flat">
                                </v-data-table>
                                <template v-slot:actions>
                                    <v-btn class="ml-auto" variant="elevated" :color="colorWestec"
                                        @click="isActive.value = false">Cerrar</v-btn>
                                </template>
                            </v-card>
                        </template>
                    </v-dialog>

                </template>

                <template #item.accion="{ item }">
                    <v-btn class="mr-2" text="Editar" flat density="comfortable" :color="colorWestec"
                        @click="console.log(item)">
                        <template #append>
                            <v-icon>mdi-pencil</v-icon>
                        </template>
                    </v-btn>
                </template>

                <template #footer.prepend>

                    <v-dialog persistent width="80%" height="100%">
                        <template v-slot:activator="{ props: activatorProps }">
                            <div class="mr-auto">
                                <v-btn v-bind="activatorProps" class="mx-4 my-5" text="Agregar contacto" height="50px"
                                    density="default" :color="colorWestec" @click="">
                                    <template #append>
                                        <v-icon class="mr-2">mdi-account-multiple-plus</v-icon>
                                    </template>
                                </v-btn>
                            </div>
                        </template>
                        <template v-slot:default="{ isActive }">
                            <v-card class="px-14 pt-3 d-flex flex-row justify-content-start align-center " prepend-icon="" rounded="b-0" :color="colorWestec"
                                height="125px" width="100%">
                                <div class="">
                                    <div class="d-flex gap-2">
                                        <v-icon size="30">mdi-account-plus</v-icon>
                                        <h4>Agregar contacto</h4>
                                    </div>
                                    <p>agregue su contacto con la informacion proporcionada</p>
                                </div>
                                <v-btn class="ml-auto mb-3" variant="flat" icon="mdi-close"
                                 @click="isActive.value = false" :color="colorWestec">
                                </v-btn>
                            </v-card>

                            <v-card class="p-4 d-flex justify-content-start align-start rounded-t-0" rounded="lg"
                                color="white" height="100%">
                                <!-- aqui va la info de contacto -->
                                <div class="d-flex align-center justify-content-center">

                                    <form method="POST" @submit.prevent="registrarContacto" class="row">
                                        <p class="m-0 ml-auto">Todos los campos con <span style="color: red">*</span>
                                            son necesarios</p>
                                        <div class="my-2 col-6">
                                            <v-text-field class="custom-label-asterisco" id="nombresContacto"
                                                v-model="credencialesContacto.nombre"
                                                :error-messages="v$.credencialesContacto.nombre.$errors.map(e => e.$message)"
                                                label="Nombres" rounded="lg" variant="outlined" density="comfortable"
                                                prepend-inner-icon="mdi-account"></v-text-field>
                                        </div>
                                        <div class="my-2 col-6">
                                            <v-text-field class="custom-label-asterisco" id="apellidosContacto"
                                                v-model="credencialesContacto.apellido"
                                                :error-messages="v$.credencialesContacto.apellido.$errors.map(e => e.$message)"
                                                label="Apellidos" rounded="lg" variant="outlined" density="comfortable"
                                                prepend-inner-icon="mdi-account"></v-text-field>
                                        </div>
                                        <div class="my-2 col-2">
                                            <v-select v-model="credencialesContacto.tipo_identificacion"
                                                :items="tipoIdentificaciones" item-title="nombre" item-value="id"
                                                :prepend-inner-icon="credencialesContacto.tipo_identificacion == 2 ? 'mdi-passport' : 'mdi-id-card'"
                                                :error-messages="v$.credencialesContacto.tipo_identificacion.$errors.map(e => e.$message)"
                                                variant="outlined" rounded="lg" label="Tipo de identificacion"
                                                density="comfortable">
                                            </v-select>
                                        </div>
                                        <div class="my-2 col-4">
                                            <v-text-field class="custom-label-asterisco" id="identificacionContacto"
                                                v-model="credencialesContacto.identificacion"
                                                :error-messages="v$.credencialesContacto.identificacion.$errors.map(e => e.$message)"
                                                label="Documento identificador" rounded="lg" variant="outlined"
                                                density="comfortable"></v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-text-field class="custom-label-asterisco" id="correo"
                                                v-model="credencialesContacto.correo"
                                                :error-messages="v$.credencialesContacto.correo.$errors.map(e => e.$message)"
                                                label="Correo Electrónico" rounded="lg" variant="outlined"
                                                density="comfortable" prepend-inner-icon="mdi-email"></v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-text-field v-model="credencialesContacto.password"
                                                class="custom-label-asterisco" label="Contraseña"
                                                :error-messages="v$.credencialesContacto.password.$errors.map(e => e.$message)"
                                                @blur="" rounded="lg"
                                                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                                                :type="visible ? 'text' : 'password'" density="comfortable"
                                                prepend-inner-icon="mdi-lock-outline" variant="outlined"
                                                @click:append-inner="visible = !visible"></v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-text-field v-model="credencialesContacto.password_confirm"
                                                class="custom-label-asterisco" label="Confirmar contraseña"
                                                :error-messages="v$.credencialesContacto.password_confirm.$errors.map(e => e.$message)"
                                                :append-inner-icon="visible2 ? 'mdi-eye-off' : 'mdi-eye'"
                                                :type="visible2 ? 'text' : 'password'" rounded="lg"
                                                density="comfortable" prepend-inner-icon="mdi-lock-outline"
                                                variant="outlined" @blur=""
                                                @click:append-inner="visible2 = !visible2"></v-text-field>
                                        </div>
                                        <div class="my-2 col-6">
                                            <v-autocomplete class="custom-label-asterisco"
                                                v-model="credencialPaisWatcher" :loading="loadingPais" :items="paises"
                                                :item-title="$i18n.locale == 'es' ? 'nombre' : 'nombre_en'"
                                                return-object prepend-inner-icon="mdi-flag-variant"
                                                :error-messages="v$.credencialesContacto.pais.$errors.map(e => e.$message)"
                                                density="comfortable" variant="outlined" rounded="lg" label="Pais">
                                            </v-autocomplete>
                                        </div>
                                        <div class="my-2 col-3">
                                            <v-autocomplete id="estadosId" v-model="credencialEstadoWatcher"
                                                :loading="loadingEstado" :items="estados" item-title="name"
                                                return-object :disabled="estadoDisable"
                                                :hint="credencialesContacto.estado == '---' ? 'Este pais no tiene estados' : ''"
                                                density="comfortable" persistent-hint
                                                :error-messages="v$.credencialesContacto.estado.$errors.map(e => e.$message)"
                                                variant="outlined" rounded="lg" label="Estado"></v-autocomplete>
                                        </div>

                                        <div class="my-2 col-3">
                                            <v-autocomplete v-model="credencialesContacto.ciudad"
                                                :loading="loadingCiudad" :items="ciudades" item-title="name"
                                                item-value="name" :disabled="ciudadDisable"
                                                :hint="credencialesContacto.ciudad == '---' ? 'Este estado no tiene ciudades' : ''"
                                                density="comfortable" persistent-hint
                                                :error-messages="v$.credencialesContacto.ciudad.$errors.map(e => e.$message)"
                                                variant="outlined" rounded="lg" label="Ciudad"></v-autocomplete>
                                        </div>

                                        <div class="my-2 col-12">
                                            <v-text-field class="custom-hint-asterisco" id="telefono"
                                                v-model="credencialesContacto.telefono"
                                                :error-messages="v$.credencialesContacto.telefono.$errors.map(e => e.$message)"
                                                hint="Telefono" persistent-hint label="Telefono" rounded="lg"
                                                variant="outlined" density="comfortable" append-inner-icon="mdi-phone"
                                                :key="maskPais" v-mask="maskPais">

                                                <template #label>
                                                    <div class=" d-flex align-center justify-content-center">
                                                        <v-icon size="20px">mdi-plus</v-icon> <span
                                                            style="margin-bottom: 2px;">{{ `${numeroPais}` }}</span>
                                                    </div>

                                                </template>
                                            </v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-text-field class="custom-label-asterisco" id="direccion1"
                                                v-model="credencialesContacto.direccion1"
                                                :error-messages="v$.credencialesContacto.direccion1.$errors.map(e => e.$message)"
                                                label="Direccion 1" rounded="lg" variant="outlined"
                                                density="comfortable"
                                                prepend-inner-icon="mdi-map-marker"></v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-text-field id="direccion2" v-model="credencialesContacto.direccion2"
                                                :error-messages="v$.credencialesContacto.direccion2.$errors.map(e => e.$message)"
                                                label="Direccion 2" rounded="lg" variant="outlined"
                                                density="comfortable"
                                                prepend-inner-icon="mdi-map-marker"></v-text-field>
                                        </div>


                                        <div class="my-2 col-6">
                                            <v-text-field class="custom-label-asterisco" id="empresa"
                                                v-model="credencialesContacto.empresa"
                                                :error-messages="v$.credencialesContacto.empresa.$errors.map(e => e.$message)"
                                                label="Empresa" rounded="lg" variant="outlined" density="comfortable"
                                                prepend-inner-icon="mdi-domain"></v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-text-field id="cargo" v-model="credencialesContacto.cargo"
                                                :error-messages="v$.credencialesContacto.cargo.$errors.map(e => e.$message)"
                                                label="Cargo" rounded="lg" variant="outlined" density="comfortable"
                                                prepend-inner-icon="mdi-account"></v-text-field>
                                        </div>

                                        <div class="my-2 col-6">
                                            <v-autocomplete id="areaempresa" class="custom-label-asterisco"
                                                v-model="credencialesContacto.areaEmpresa"
                                                prepend-inner-icon="mdi-account" :items="areasContactos"
                                                item-title="nombre" item-value="id" density="comfortable"
                                                :error-messages="v$.credencialesContacto.areaEmpresa.$errors.map(e => e.$message)"
                                                variant="outlined" rounded="lg" label="Area empresa">
                                            </v-autocomplete>
                                        </div>

                                        <div class="my-2 mb-8">

                                            <v-btn block :color="colorWestec" size="large" rounded="lg" type="submit"
                                                variant="flat">
                                                Registrar
                                            </v-btn>
                                            <div class="d-flex align-center justify-content-start mb-0 mt-6">
                                                <v-btn class="" color="error" rounded="lg" @click="limpiarCredenciales"
                                                    variant="flat">
                                                    Limpiar todo
                                                </v-btn>

                                            </div>
                                        </div>
                                    </form>
                                </div>

                            </v-card>

                        </template>
                    </v-dialog>
                </template>
            </v-data-table>
            <div v-else class="d-flex align-center justify-content-center">
                <v-card class="text-h5 p-4 d-flex align-center justify-content-center" border width="100%">
                    <div class="w-75 bold text-center">
                        Usted actualmente no cuenta con contactos
                    </div>
                </v-card>
            </div>

        </div>
        <div v-else class="my-12 mx-16 d-flex align-center justify-content-center"
            style="height: 85vh; padding-bottom: 100px;">
            <v-progress-circular :size="200" :width="7" :color="colorWestec"
                indeterminate>cargando...</v-progress-circular>
        </div>
    </v-fade-transition>

</template>

<style>
.v-text-field--outlined fieldset {
    border: blue 2px solid !important;
}
</style>

<script>

import { useUserStore } from '../../stores/user'
import * as dominiosService from '../../services/dominios.js'
import * as infoUsuarioService from '../../services/userinfo.js'
import * as paisesService from "../../services/paises"
import * as mensajes from '../../helpers/mensajes'
import useValidate from '@vuelidate/core'
import { required, helpers, minLength, sameAs, email, numeric } from '@vuelidate/validators'
import { mask } from 'vue-the-mask'
import { setTransitionHooks } from 'vue'

export default {
    setup() {
        const userStore = useUserStore()
        return { userStore }
    },
    directives: {
        // Define una directiva personalizada para la máscara de entrada
        mask: (el, binding) => {
            if (!binding.value) return; // Si no hay valor de binding, retorna
            mask(el, binding); // Aplica la máscara al elemento DOM
        }
    },
    data() {
        return {
            v$: useValidate(),
            loading: true,
            showAnim: false,
            readOnly: true,
            usuario: {
                nombre: '',
                apellido: '',
                identificacion: '',
                pais: '',
                estado: '',
                ciudad: '',
                email: '',
                telefono: '',
                direccion1: '',
                direccion2: '',
                empresa: '',
                cargo: '',
            },

            visible: false,
            visible2: false,
            estadoDisable: true,
            ciudadDisable: true,
            loadingPais: true,
            loadingEstado: false,
            loadingCiudad: false,
            credencialPaisWatcher: null,
            credencialEstadoWatcher: null,
            isoPais: '',
            isoEstado: '',
            numeroPais: '',
            maskPais: '',
            credencialesContacto: {
                nombre: '',
                apellido: '',
                tipo_identificacion: '',
                identificacion: '',
                correo: '',
                password: '',
                password_confirm: '',
                pais: '',
                telefono: '',
                ubicacion_id: '',
                estado: null,
                ciudad: null,
                direccion1: '',
                direccion2: '',
                empresa: '',
                areaEmpresa: null,
                cargo: '',
            },
            paises: [],
            estados: [],
            ciudades: [],

            // Máscara de códigos de teléfono por país
            maskPhoneCode: {
                "PA": "6###-####",
                "US": "(###) ###-####",
            },

            tipoIdentificaciones: [],
            contactosUsuario: [],
            areasContactos: [],
            search: '',
            headers: [
                { title: 'Nombre', align: 'start', key: 'nombre' },
                { title: 'Correo', key: 'email' },
                { title: 'Telefono', key: 'telefono' },
                { title: 'Representante Legal', key: 'representante_legal' },
                { title: 'Ciudad', key: 'ciudad' },
                { title: 'Estado', key: 'estado' },
                { title: 'Dominios de contacto', key: 'contactos_dominios' },
                { title: 'Acciones', key: 'accion' }
            ],
            headersDominioContacto: [
                { title: 'Dominio', align: 'start', key: 'nombre_dominio' },
                { title: 'Tipo de contacto', key: 'tipo_contacto.nombre' },
                { title: 'Abreviatura', key: 'tipo_contacto.abreviatura' },
                { title: 'Estatus', key: 'tipo_contacto.estatus' },

            ],
        }
    },
    watch: {
        // Observadores de cambios en las variables credencialPaisWatcher y credencialEstadoWatcher
        'credencialPaisWatcher'(paisNuevo) {
            // Observa los cambios en el país seleccionado
            if (paisNuevo != null) {
                // Si se selecciona un nuevo país
                this.credencialEstadoWatcher = null; // Reinicia el observador de estado
                this.estados = []; // Reinicia la lista de estados
                this.credencialesContacto.estado = ''; // Reinicia el estado seleccionado
                this.ciudades = []; // Reinicia la lista de ciudades
                this.credencialesContacto.ciudad = ''; // Reinicia la ciudad seleccionada
                this.numeroPais = paisNuevo.codigo_telefonico

                if (paisNuevo.abreviatura in this.maskPhoneCode) {
                    this.maskPais = this.maskPhoneCode[paisNuevo.abreviatura]
                } else {
                    // De lo contrario, no se aplica ningún formato de teléfono
                    this.maskPais = '';
                }
                this.credencialesContacto.ubicacion_id = paisNuevo.id;
                this.credencialesContacto.pais = this.$i18n.locale == 'es' ? paisNuevo.nombre : paisNuevo.nombre_en; // Establece el nombre del país seleccionado
                this.isoPais = paisNuevo.abreviatura; // Establece el código ISO del país seleccionado
                this.GetStatesofCountry(this.isoPais); // Obtiene los estados del país seleccionado
                this.estadoDisable = false; // Habilita la selección de estado
            } else {
                // Si no se selecciona un país
                this.estadoDisable = true; // Deshabilita la selección de estado
                this.estados = []; // Reinicia la lista de estados
                this.credencialesContacto.estado = ''; // Reinicia el estado seleccionado
                this.numeroPais = ''; // Reinicia el código de país
            }
        },
        'credencialEstadoWatcher'(estadoNuevo) {
            // Observa los cambios en el estado seleccionado
            if (estadoNuevo != null) {
                // Si se selecciona un nuevo estado
                this.ciudades = []; // Reinicia la lista de ciudades
                this.credencialesContacto.ciudad = ''; // Reinicia la ciudad seleccionada
                this.credencialesContacto.estado = estadoNuevo.name; // Establece el nombre del estado seleccionado
                this.isoEstado = estadoNuevo.iso2; // Establece el código ISO del estado seleccionado
                this.GetCitiesbyStateCountry(this.isoPais, this.isoEstado); // Obtiene las ciudades del país y estado seleccionados
                this.ciudadDisable = false; // Habilita la selección de ciudad
            } else {
                // Si no se selecciona un estado
                this.ciudadDisable = true; // Deshabilita la selección de ciudad
                this.ciudades = []; // Reinicia la lista de ciudades
                this.credencialesContacto.ciudad = ''; // Reinicia la ciudad seleccionada
            }
        },
    },
    validations() {
        const containsMask = (value) => {
            // Validaciones para los campos del formulario
            if (this.maskPais == '') {
                // Si la máscara del país está vacía, valida si el valor es numérico
                return /^\d+$/.test(value);
            } else {
                // Si la máscara del país no está vacía, no se necesita validación numérica
                return true;
            }
        }

        return {
            credencialesContacto: {
                nombre: {
                    required: helpers.withMessage('Valor requerido', required),
                },
                apellido: {
                    required: helpers.withMessage('Valor requerido', required),
                },
                tipo_identificacion: {
                    required: helpers.withMessage('Valor requerido', required),
                },
                identificacion: {
                    required: helpers.withMessage('Valor requerido', required),
                    containsCedula: helpers.withMessage(
                        () => 'La identificacion debe contener solo Mayusculas, numeros o "-" en medio',
                        (value) => /^(?!-)(?!.*-$)[A-Z0-9-]+$/.test(value)
                    ),
                },
                correo: {
                    required: helpers.withMessage('Valor requerido', required),
                    email: helpers.withMessage('El valor no es un email valido', email),
                },
                password: {
                    required: helpers.withMessage('Valor requerido', required),
                    minLength: helpers.withMessage('La contraseña debe tener un mínimo de seis caracteres', minLength(6)),
                    containsPasswordRequirement: helpers.withMessage(
                        () => `La contraseña debe tener mínimo un caracter en mayúscula, minúscula, uno especial y un número`,
                        (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])/.test(value)
                    ),
                },
                password_confirm: {
                    required: helpers.withMessage('Valor requerido', required),
                    sameAsPassword: helpers.withMessage('Las contraseñas deben coincidir', sameAs(this.credencialesContacto.password)),
                    minLength: helpers.withMessage('La contraseña debe tener un mínimo de seis caracteres', minLength(6)),
                    containsPasswordRequirement: helpers.withMessage(
                        () => `La contraseña debe tener mínimo un caracter en mayúscula, minúscula, uno especial y un número`,
                        (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])/.test(value),
                    ),
                },
                pais: {
                    required: helpers.withMessage('Valor requerido', required),
                },
                estado: {

                },
                ciudad: {

                },
                telefono: {
                    required: helpers.withMessage('Valor requerido', required),
                    containsMask: helpers.withMessage('El valor debe ser numerico', containsMask),
                },
                direccion1: {
                    required: helpers.withMessage('Valor requerido', required),
                },
                direccion2: {

                },
                empresa: {
                    required: helpers.withMessage('Valor requerido', required),
                },
                cargo: {

                },
                areaEmpresa: {
                    required: helpers.withMessage('Valor requerido', required),
                }

            }
        }
    },
    methods: {
        editProfile() {
            this.readOnly = !this.readOnly
        },
        registrarContacto() {
            // Método para registrar un usuario
            this.v$.$touch(); // Activa la validación de formularios
            console.log(this.credencialesContacto)
            if (!this.v$.$error) {

                if (this.credencialesContacto.estado == '---') {
                    this.credencialesContacto.estado == null;
                }
                if (this.credencialesContacto.ciudad == '---') {
                    this.credencialesContacto.ciudad == null;
                }
                // Si no hay errores de validación
                this.credencialesContacto.telefono = `+${this.numeroPais} ${this.credencialesContacto.telefono}`; // Formatea el teléfono con el código de país
            }
        },

        async getuserContacts() {
            let info = {
                //userId: this.userStore.id_acceso
                userId: 4624
            }
            await infoUsuarioService
                .getuserContacts(info)
                .then((response) => {
                    if (response.status == 200) {
                        this.contactosUsuario = response.payload;
                        console.log(this.contactosUsuario)
                    }
                    else {
                        mensajes.ShowMessages(response)
                    }
                    this.loading = false;
                    this.showAnim = true;
                })
                .catch((err) => console.log(err))

        },

        async getAreasContacts() {
            await infoUsuarioService
                .getTiposAreasEmpresas()
                .then((response) => {
                    if (response.status == 200) {
                        this.areasContactos = response.payload;
                    } else {
                        mensajes.ShowMessages(response)
                    }
                })
                .catch((err) => console.log(err))
        },
        getTipoIdenficaciones() {
            infoUsuarioService.getTipoIdentificaciones()
                .then((response) => {
                    if (response.status == 200) {
                        this.tipoIdentificaciones = response.payload;
                    } else {
                        mensajes.ShowMessages(response)
                    }
                })
                .catch((err) => console.log(err))
        },
        // Método para obtener la lista de países
        async GetCountries() {
            await infoUsuarioService
                .getUbicaciones()
                .then((response) => {
                    let aux = response.payload;
                    // Itera sobre la lista de países
                    aux.forEach((country, index) => {
                        // Si el país es Panamá o Estados Unidos
                        if (country.id == 240) {
                            const paisPro = aux[index];
                            aux.splice(index, 1);
                            aux.unshift(paisPro);
                            //pone a Estados Unidos y Panama de primeros en la lista
                        }
                    });
                    aux.forEach((country, index) => {
                        // Si el país es Panamá o Estados Unidos
                        if (country.id == 173) {
                            const paisPro = aux[index];
                            aux.splice(index, 1);
                            aux.unshift(paisPro);
                            //pone a Estados Unidos y Panama de primeros en la lista
                        }
                    });
                    this.paises = aux; // Asigna la lista de países al componente
                    this.loadingPais = false; // Indica que la carga de países ha finalizado
                })
                .catch((err) => console.log(err))
        },

        // Método para obtener los estados de un país
        GetStatesofCountry(country) {
            this.loadingEstado = true;
            paisesService
                .getStatesofCountry(country)
                .then((response) => {
                    //let infoPais = [];
                    this.estados = JSON.parse(response.states)
                    // Si no hay estados
                    if (this.estados.length == 0) {
                        // asigna valores por defecto y deshabilita el input
                        this.credencialesContacto.estado = '---'
                        this.credencialesContacto.ciudad = '---'
                        this.estadoDisable = true;
                    }

                    this.loadingEstado = false;
                })
                .catch((err) => console.log(err))
        },

        // Método para obtener las ciudades de un estado en un país
        GetCitiesbyStateCountry(country, estado) {
            this.loadingCiudad = true;
            paisesService
                .getCitiesbyStateCountry(country, estado)
                .then((response) => {
                    this.ciudades = response.payload;
                    // Si no hay ciudades
                    if (this.ciudades.length == 0) {
                        // asigna valor por defecto y deshabilita el input
                        this.credencialesContacto.ciudad = '---'
                        this.ciudadDisable = true;
                    }
                    this.loadingCiudad = false;
                })
                .catch((err) => console.log(err))
        },

        limpiarCredenciales() {
            this.v$.$reset(); // Reinicia la validación de formularios
            this.credencialPaisWatcher = null,
                this.credencialEstadoWatcher = null,
                this.isoPais = '',
                this.isoEstado = '',
                this.numeroPais = '',
                this.credencialesContacto = {
                    nombre: '',
                    apellido: '',
                    identificacion: '',
                    correo: '',
                    pais: '',
                    estado: '',
                    ciudad: '',
                    password: '',
                    password_confirm: '',
                    direccion1: '',
                    direccion2: '',
                    empresa: '',
                    cargo: '',
                }
        },
        async inicializaciones() {

            await infoUsuarioService
                .getUbicacion(this.$i18n.locale, this.userStore.id_ubicacion)
                .then((response) => this.usuario.pais = response.payload)
                .catch((err) => console.log(err))

            document.getElementById('carritoId').classList.remove('d-none')
            this.usuario.nombre = this.userStore.nombre
            this.usuario.apellido = this.userStore.apellido
            this.usuario.identificacion = this.userStore.identificacion
            this.usuario.estado = this.userStore.estado
            this.usuario.ciudad = this.userStore.ciudad
            this.usuario.email = this.userStore.email
            this.usuario.telefono = this.userStore.telefono
            this.usuario.direccion1 = this.userStore.direccion1
            this.usuario.direccion2 = this.userStore.direccion2
            this.usuario.empresa = this.userStore.empresa
            this.usuario.cargo = this.userStore.cargo
        },
    },
    async mounted() {
        this.inicializaciones();
        await this.getAreasContacts();
        await this.getuserContacts();
        await this.GetCountries();
        this.getTipoIdenficaciones();
    }

}

</script>