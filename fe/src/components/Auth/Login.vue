<template>
    <div class="marginTopBot d-flex align-center justify-content-center">

        <div class="d-flex flex-column align-center justify-content-center py-5">

            <v-card class="p-5" elevation="8" width="448px" rounded="lg" border>

                <div class="d-flex align-center justify-content-center mb-6">
                    <img class="logo2" src="/src/static/img/nicpa.png" alt="nicPa" />
                </div>

                <v-text-field class="my-4" label="Email" v-model="credenciales.email"
                    :error-messages="v$.credenciales.email.$errors.map(e => e.$message)" rounded="lg"
                    placeholder="Email address" prepend-inner-icon="mdi-email-outline" density="comfortable"
                    variant="outlined"></v-text-field>

                <v-text-field class="mb-2" label="Contraseña" v-model="credenciales.password"
                    :error-messages="v$.credenciales.password.$errors.map(e => e.$message)"
                    :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
                    rounded="lg" density="comfortable" placeholder="Enter your password"
                    prepend-inner-icon="mdi-lock-outline" variant="outlined"
                    @click:append-inner="visible = !visible"></v-text-field>


                <v-alert v-model="error.status" class="mb-8" prominent :color="error.color" :text="error.titulo"
                    border="start" closable close-label="Close Alert" :type="error.type ? error.type : null"
                    density="compact"></v-alert>




                <v-btn block class="mb-8" :color="colorWestec" size="large" @click="tryLoginUsuario()" variant="flat">
                    Iniciar sesion
                </v-btn>

                <div class="d-flex align-center justify-content-center">
                    <v-btn class="text-caption text-blue mb-1" variant="text"
                        @click="">
                        Olvidaste tu contraseña?</v-btn>
                </div>

                <div class="d-flex justify-content-center">
                    <v-btn class="text-center text-blue text-decoration-none"
                        @click="" variant="text">
                        Registrate ahora<v-icon icon="mdi-chevron-right" link></v-icon>
                    </v-btn>
                </div>
                <v-card class="my-4" color="surface-variant" variant="tonal">
                    <v-card-text class="text-medium-emphasis text-caption text-center">
                        Al continuar, estás confirmando que has leído nuestros Términos y condiciones y política de
                        cookies
                    </v-card-text>
                </v-card>

            </v-card>
        </div>
    </div>
</template>
<style>
.marginTopBot {
    height: 100vh;
    padding-top: 25px;
    padding-bottom: 25px;
    background-image: url('../../static/img/backgroundAUTH.svg');
    background-attachment: fixed;
    background-size: cover;
}
</style>
<script>

import { useUserStore } from '../../stores/user';
import useValidate from '@vuelidate/core'
import { email, required, helpers } from '@vuelidate/validators'
import * as mensajes from "../../helpers/mensajes";

export default {
    setup() {
        // Obtenemos la instancia de useUserStore
        const userStore = useUserStore();
        // Retornamos Tr y userStore para que estén disponibles en el componente
        return { userStore }
    },
    data() {
        return {
            // Instancia de vuelidate
            v$: useValidate(),
            visible: false,
            credenciales: {
                email: '',
                password: '',
            },
            error: {
                status: false,
                titulo: '',
                type: '',
                color: '',
            },
        }
    },

    validations() {
        return {
            credenciales: {
                email: {
                    required: helpers.withMessage('Valor requerido', required),
                    email: helpers.withMessage('El valor no es un email valido', email),
                },
                password: {
                    required: helpers.withMessage('Valor requerido', required),
                },
            }
        }
    },
    methods: {
        tryLoginUsuario() {
            try {

                // Marcamos los campos como "touched" para activar las validaciones
                this.v$.$touch()

                // Verificamos si hay errores de validación
                if (!this.v$.$error) {
                    // Codificamos la contraseña a base64
                    const contrabase64 = btoa(this.credenciales.password)

                    // Objeto con las credenciales para iniciar sesión
                    const loginTry = {
                        email: this.credenciales.email,
                        password: contrabase64
                    }

                    // Intentamos iniciar sesión a través de la instancia de userStore
                    this.userStore
                        .login(loginTry)
                        .then((res) => {
                            // Si la respuesta es exitosa
                            if (res.status == 200) {
                                // Redirigimos al usuario a la página de inicio
                                this.$router.push('/')
                                // Mostramos un mensaje de éxito
                                mensajes.showMessagesLong('Logueado exitosamente', 'success')
                            }
                            // Si las credenciales son incorrectas
                            else {
                                // Configuramos el objeto de error
                                this.error = {
                                    status: true,
                                    titulo: 'Credenciales incorrectos',
                                    type: 'error',
                                    color: 'red-accent-4',
                                }

                            }
                        })
                }
            }
            catch (error) {
                // Capturamos cualquier error que ocurra durante el proceso de inicio de sesión
                if (error.name == 'InvalidCharacterError') {
                    // Manejamos errores específicos
                    mensajes.toastr('Error', 'Caracteres invalidos', 'error')
                } else {
                    mensajes.toastr('Error', '', 'error')
                }
            }
        },
    },
}
</script>
