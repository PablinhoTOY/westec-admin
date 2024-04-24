<template>
  <div class="marginTopBot" style="height: auto;">

    <div class="d-flex flex-column align-center justify-content-center">

      <v-card class="p-5" elevation="8" width="80vw" rounded="lg" border>
        <v-btn id="" variant="flat" size="72" rounded="circle" to=""><v-icon
            color="#5c5c5c" size="56">mdi-arrow-left-bold</v-icon></v-btn>
        <div class="mb-8 d-flex align-center justify-content-center">
          <h2 class="nic2" style="text-shadow: 0 0">Registro Westec </h2>
        </div>

        <div class="d-flex align-center justify-content-center">
          <form method="POST" @submit.prevent="registrarUsuario" class="row">
            <p class="m-0 ml-auto">Todos los campos con <span style="color: red">*</span> son necesarios</p>
            <div class="my-2 col-6">
              <v-text-field class="custom-label-asterisco" id="nombres" v-model="credenciales.nombre"
                :error-messages="v$.credenciales.nombre.$errors.map(e => e.$message)" label="Nombres" rounded="lg"
                variant="outlined" density="comfortable" prepend-inner-icon="mdi-account"></v-text-field>
            </div>
            <div class="my-2 col-6">
              <v-text-field class="custom-label-asterisco" id="apellidos" v-model="credenciales.apellido"
                :error-messages="v$.credenciales.apellido.$errors.map(e => e.$message)" label="Apellidos" rounded="lg"
                variant="outlined" density="comfortable" prepend-inner-icon="mdi-account"></v-text-field>
            </div>

            <div class="my-2 col-2">
              <v-select v-model="credenciales.tipoIdentificacion" :items="tipoIdentificaciones" item-title="nombre"
                item-value="id" :onchange="console.log(credenciales.tipoIdentificacion)"
                :prepend-inner-icon="credenciales.tipoIdentificacion == 2 ? 'mdi-passport' : 'mdi-id-card'"
                :error-messages="v$.credenciales.tipoIdentificacion.$errors.map(e => e.$message)"
                variant="outlined" rounded="lg" label="Tipo de identificacion" density="comfortable">
              </v-select>
            </div>
            <div class="my-2 col-4">
              <v-text-field class="custom-label-asterisco" id="identificacion" v-model="credenciales.identificacion"
                :error-messages="v$.credenciales.identificacion.$errors.map(e => e.$message)"
                label="Documento identificador" rounded="lg" variant="outlined" density="comfortable"></v-text-field>
            </div>

            <div class="my-2 col-6">
              <v-text-field class="custom-label-asterisco" id="correo" v-model="credenciales.correo"
                :error-messages="v$.credenciales.correo.$errors.map(e => e.$message)" label="Correo Electrónico"
                rounded="lg" variant="outlined" density="comfortable" prepend-inner-icon="mdi-email"></v-text-field>
            </div>

            <div class="my-2 col-6">
              <v-text-field v-model="credenciales.password" class="custom-label-asterisco" label="Contraseña"
                :error-messages="v$.credenciales.password.$errors.map(e => e.$message)" @blur="" rounded="lg"
                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
                density="comfortable" prepend-inner-icon="mdi-lock-outline" variant="outlined"
                @click:append-inner="visible = !visible"></v-text-field>
            </div>

            <div class="my-2 col-6">
              <v-text-field v-model="credenciales.password_confirm" class="custom-label-asterisco"
                label="Confirmar contraseña"
                :error-messages="v$.credenciales.password_confirm.$errors.map(e => e.$message)"
                :append-inner-icon="visible2 ? 'mdi-eye-off' : 'mdi-eye'" :type="visible2 ? 'text' : 'password'"
                rounded="lg" density="comfortable" prepend-inner-icon="mdi-lock-outline" variant="outlined" @blur=""
                @click:append-inner="visible2 = !visible2"></v-text-field>
            </div>
            <div class="my-2 col-6">
              <v-autocomplete class="custom-label-asterisco" v-model="credencialPaisWatcher" :loading="loadingPais"
                :items="paises" item-title="nombre" return-object
                :error-messages="v$.credenciales.pais.$errors.map(e => e.$message)" variant="outlined" rounded="lg"
                label="Pais" prepend-inner-icon="mdi-flag-variant">
              </v-autocomplete>
            </div>
            <div class="my-2 col-3">
              <v-autocomplete id="estadosId" v-model="credencialEstadoWatcher" :loading="loadingEstado" :items="estados"
                item-title="name" return-object :disabled="estadoDisable"
                :hint="credenciales.estado == '---' ? 'Este pais no tiene estados' : ''" persistent-hint
                :error-messages="v$.credenciales.estado.$errors.map(e => e.$message)" variant="outlined" rounded="lg"
                label="Estado"></v-autocomplete>
            </div>

            <div class="my-2 col-3">
              <v-autocomplete v-model="credenciales.ciudad" :loading="loadingCiudad" :items="ciudades" item-title="name"
                item-value="name" :disabled="ciudadDisable"
                :hint="credenciales.ciudad == '---' ? 'Este estado no tiene ciudades' : ''" persistent-hint
                :error-messages="v$.credenciales.ciudad.$errors.map(e => e.$message)" variant="outlined" rounded="lg"
                label="Ciudad"></v-autocomplete>
            </div>

            <div class="my-2 col-12">
              <v-text-field class="custom-hint-asterisco" id="telefono" v-model="credenciales.telefono"
                :error-messages="v$.credenciales.telefono.$errors.map(e => e.$message)" hint="Telefono" persistent-hint
                label="Telefono" rounded="lg" variant="outlined" density="comfortable" append-inner-icon="mdi-phone"
                :key="maskPais" v-mask="maskPais">

                <template #label>
                  <div class=" d-flex align-center justify-content-center">
                    <v-icon size="20px">mdi-plus</v-icon> <span style="margin-bottom: 2px;">{{ `${numeroPais}` }}</span>
                  </div>

                </template>
              </v-text-field>
            </div>

            <div class="my-2 col-6">
              <v-text-field class="custom-label-asterisco" id="direccion1" v-model="credenciales.direccion1"
                :error-messages="v$.credenciales.direccion1.$errors.map(e => e.$message)" label="Direccion 1"
                rounded="lg" variant="outlined" density="comfortable"
                prepend-inner-icon="mdi-map-marker"></v-text-field>
            </div>

            <div class="my-2 col-6">
              <v-text-field id="direccion2" v-model="credenciales.direccion2"
                :error-messages="v$.credenciales.direccion2.$errors.map(e => e.$message)" label="Direccion 2"
                rounded="lg" variant="outlined" density="comfortable"
                prepend-inner-icon="mdi-map-marker"></v-text-field>
            </div>


            <div class="my-2 col-6">
              <v-text-field class="custom-label-asterisco" id="empresa" v-model="credenciales.empresa"
                :error-messages="v$.credenciales.empresa.$errors.map(e => e.$message)" label="Empresa" rounded="lg"
                variant="outlined" density="comfortable" prepend-inner-icon="mdi-domain"></v-text-field>
            </div>

            <div class="my-2 col-6">
              <v-text-field id="cargo" v-model="credenciales.cargo"
                :error-messages="v$.credenciales.cargo.$errors.map(e => e.$message)" label="Cargo" rounded="lg"
                variant="outlined" density="comfortable" prepend-inner-icon="mdi-account"></v-text-field>
            </div>

            <div class="my-2 mb-8">
              <div class="d-flex align-center justify-content-start mt-0 mb-8">
                <v-btn class="" color="error" rounded="lg" @click="limpiarCredenciales" variant="flat">
                  Limpiar todo
                </v-btn>

              </div>
              <v-btn block :color="colorWestec" size="large" rounded="lg" type="submit" variant="flat">
                Registrar
              </v-btn>
            </div>
          </form>
        </div>

      </v-card>
    </div>
  </div>
</template>

<style>
.v-field--disabled-numeroTelefono {
  pointer-events: none;
}

.custom-label-asterisco .v-label::after {
  content: '*';
  color: red;
  opacity: 1;
}

.custom-hint-asterisco .v-messages__message::after {
  content: '*';
  color: red;
  opacity: 1;
}
</style>

<script>
import { useUserStore } from '../../stores/user';
import * as mensajes from "../../helpers/mensajes";
import * as infoUsuarioService from '../../services/userinfo.js'
import * as paisesService from "../../services/paises"
import useValidate from '@vuelidate/core'
import { required, helpers, minLength, sameAs, email, numeric } from '@vuelidate/validators'
import { mask } from 'vue-the-mask'


export default {
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },
  directives: {
    // Define una directiva personalizada para la máscara de entrada
    mask: (el, binding) => {
      if (!binding.value) return; // Si no hay valor de binding, retorna
      mask(el, binding); // Aplica la máscara al elemento DOM
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
        this.credenciales.estado = ''; // Reinicia el estado seleccionado
        this.ciudades = []; // Reinicia la lista de ciudades
        this.credenciales.ciudad = ''; // Reinicia la ciudad seleccionada
        this.numeroPais = paisNuevo.codigo_telefonico

        if (paisNuevo.abreviatura in this.maskPhoneCode) {
          this.maskPais = this.maskPhoneCode[paisNuevo.abreviatura]
        } else {
          // De lo contrario, no se aplica ningún formato de teléfono
          this.maskPais = '';
        }
        this.credenciales.ubicacion_id = paisNuevo.id;
        this.credenciales.pais = this.$i18n.locale == 'es' ? paisNuevo.nombre : paisNuevo.nombre_en; // Establece el nombre del país seleccionado
        this.isoPais = paisNuevo.abreviatura; // Establece el código ISO del país seleccionado
        this.GetStatesofCountry(this.isoPais); // Obtiene los estados del país seleccionado
        this.estadoDisable = false; // Habilita la selección de estado
      } else {
        // Si no se selecciona un país
        this.estadoDisable = true; // Deshabilita la selección de estado
        this.estados = []; // Reinicia la lista de estados
        this.credenciales.estado = ''; // Reinicia el estado seleccionado
        this.numeroPais = ''; // Reinicia el código de país
      }
    },
    'credencialEstadoWatcher'(estadoNuevo) {
      // Observa los cambios en el estado seleccionado
      if (estadoNuevo != null) {
        // Si se selecciona un nuevo estado
        this.ciudades = []; // Reinicia la lista de ciudades
        this.credenciales.ciudad = ''; // Reinicia la ciudad seleccionada
        this.credenciales.estado = estadoNuevo.name; // Establece el nombre del estado seleccionado
        this.isoEstado = estadoNuevo.iso2; // Establece el código ISO del estado seleccionado
        this.GetCitiesbyStateCountry(this.isoPais, this.isoEstado); // Obtiene las ciudades del país y estado seleccionados
        this.ciudadDisable = false; // Habilita la selección de ciudad
      } else {
        // Si no se selecciona un estado
        this.ciudadDisable = true; // Deshabilita la selección de ciudad
        this.ciudades = []; // Reinicia la lista de ciudades
        this.credenciales.ciudad = ''; // Reinicia la ciudad seleccionada
      }
    },
  },
  data() {
    return {
      v$: useValidate(),
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
      credenciales: {
        nombre: '',
        apellido: '',
        tipoIdentificacion: '',
        identificacion: '',
        correo: '',
        password: '',
        password_confirm: '',
        pais: '',
        telefono: '',
        ubicacion_id: null,
        estado: null,
        ciudad: null,
        direccion1: '',
        direccion2: '',
        empresa: '',
        cargo: '',
      },
      paises: [],
      estados: [],
      ciudades: [],
      tipoIdentificaciones: [],

      // Máscara de códigos de teléfono por país
      maskPhoneCode: {
        "PA": "6###-####",
        "US": "(###) ###-####",
      },
    }
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
      credenciales: {
        nombre: {
          required: helpers.withMessage('Valor requerido', required),
        },
        apellido: {
          required: helpers.withMessage('Valor requerido', required),
        },
        tipoIdentificacion: {
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
          sameAsPassword: helpers.withMessage('Las contraseñas deben coincidir', sameAs(this.credenciales.password)),
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

      }
    }
  },
  methods: {
    registrarUsuario() {
      // Método para registrar un usuario
      this.v$.$touch(); // Activa la validación de formularios
      if (!this.v$.$error) {

        if (this.credenciales.estado == '---') {
          this.credenciales.estado == null;
        }
        if (this.credenciales.ciudad == '---') {
          this.credenciales.ciudad == null;
        }

        // Si no hay errores de validación
        this.credenciales.telefono = `+${this.numeroPais} ${this.credenciales.telefono}`; // Formatea el teléfono con el código de país
        this.userStore // Accede al almacenamiento de usuario
          .register(this.credenciales) // Registra al usuario con las credenciales
          .then((res) => { // Maneja la respuesta de la solicitud
            mensajes.ShowMessages(res); // Muestra mensajes según la respuesta
            if (res.status == 200) {
              // Si la respuesta es exitosa
              this.credencialPaisWatcher = null,
                this.credencialEstadoWatcher = null,
                this.isoPais = '',
                this.isoEstado = '',
                this.numeroPais = '',
                this.credenciales = {
                  nombre: '',
                  apellido: '',
                  tipoIdentificacion: '',
                  identificacion: '',
                  correo: '',
                  pais: '',
                  estado: '',
                  ciudad: '',
                  telefono: '',
                  password: '',
                  password_confirm: '',
                  direccion1: '',
                  direccion2: '',
                  empresa: '',
                  cargo: '',
                };

              // Redirige al usuario a la página de inicio de sesión
              this.$router.push("/")
            }
          })
          .catch((err) => console.log(err));
      }
    },
    limpiarCredenciales() {
      this.v$.$reset(); // Reinicia la validación de formularios
      this.credencialPaisWatcher = null,
        this.credencialEstadoWatcher = null,
        this.isoPais = '',
        this.isoEstado = '',
        this.numeroPais = '',
        this.credenciales = {
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

    getTipoIdenficaciones() {
      infoUsuarioService.getTipoIdentificaciones()
        .then((response) => {
          if (response.status == 200) {
            this.tipoIdentificaciones = response.payload;
            console.log(this.tipoIdentificaciones)
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
          console.log(aux)
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
          let infoPais = [];
          this.estados = JSON.parse(response.states)
          // Si no hay estados
          if (this.estados.length == 0) {
            // asigna valores por defecto y deshabilita el input
            this.credenciales.estado = '---'
            this.credenciales.ciudad = '---'
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
          this.ciudades = response
          // Si no hay ciudades
          if (this.ciudades.length == 0) {
            // asigna valor por defecto y deshabilita el input
            this.credenciales.ciudad = '---'
            this.ciudadDisable = true;
          }
          this.loadingCiudad = false;
        })
        .catch((err) => console.log(err))
    },
  },
  async mounted() {
    // Obtiene la lista de países al montar el componente
    await this.GetCountries();
    this.getTipoIdenficaciones();
  },
};
</script>