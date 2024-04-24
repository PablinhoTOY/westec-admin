<template>
    <div class="d-flex flex-column align-center justify-content-center marginTopBot">

        <v-card class="pa-12 pt-8" elevation="8" width="448" rounded="lg" border>

            <form class="resetpassword" @submit.prevent="reset_password">
                <input type="hidden" v-model="token">
                <h3 class="text-center bold mb-6">Recuperar Contraseña</h3>
                <v-text-field v-model="credenciales.password" class="my-8" label="Contraseña"
                    :error-messages="v$.credenciales.password.$errors.map(e => e.$message)" @blur="" rounded="lg"
                    :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
                    density="comfortable" prepend-inner-icon="mdi-lock-outline" variant="outlined"
                    @click:append-inner="visible = !visible"></v-text-field>

                <v-text-field v-model="credenciales.password_confirm" class="my-8" label="Confirmar contraseña"
                    :error-messages="v$.credenciales.password_confirm.$errors.map(e => e.$message)"
                    :append-inner-icon="visible2 ? 'mdi-eye-off' : 'mdi-eye'" :type="visible2 ? 'text' : 'password'"
                    rounded="lg" density="comfortable" prepend-inner-icon="mdi-lock-outline" variant="outlined" @blur=""
                    @click:append-inner="visible2 = !visible2"></v-text-field>

                <v-btn block class="mb-8" :color="colorWestec" size="large" type="submit" variant="flat">
                    Reiniciar contraseña
                </v-btn>
            </form>

        </v-card>
    </div>
</template>
<script>
import { useUserStore } from '../../stores/user';
import * as mensajes from '../../helpers/mensajes';
import useValidate from '@vuelidate/core'
import { required, helpers, requiredUnless, minLength, sameAs } from '@vuelidate/validators'

export default {
    setup() {
        const userStore = useUserStore();
        return { userStore };
    },
    data() {
        return {
            v$: useValidate(),
            credenciales: {
                password: '',
                password_confirm: '',
            },
            token: '',
            visible: false,
            visible2: false,
        };
    },
    validations() {
        return {
            credenciales: {
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
            }
        }
    },
    methods: {
        reset_password() {
            this.v$.$touch()
            if (!this.v$.$error) {
                this.userStore.reset_password(this.credenciales, this.token).then(response => {
                    mensajes.ShowMessages(response);
                    if (response.status == 200) {
                        this.$router.push('/')
                    }
                })
            }
        },
    },
    mounted() {
        // Obtener el valor del token de la URL
        const token = new URLSearchParams(window.location.search).get('token')
        // Asignar el valor al input correspondiente
        if (token == null || token == '' || token == undefined) {
            this.$router.push('/')
        }
        console.log(token)
        this.token = token
    },
}
</script>