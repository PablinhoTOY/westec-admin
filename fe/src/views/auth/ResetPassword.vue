<template>
    <div class="row justify-content-center">
        <div class="col">
            <div class="card o-hidden border-0 my-5">
                <div class="card-body p-0">
                    <!-- Nested Row within Card Body -->
                    <div class="row">
                        <div class="col-lg-6 d-none d-lg-block bg-login-image2"></div>
                        <div class="col-lg-6">
                            <div class="p-5">
                                <div class="logo-div text-center">
                                    <a href="">
                                        <img class="img-fluid logo" :src="'../src/static/img/logo_utp.png'" alt="">
                                    </a>
                                </div>
                                <div class="text-center">
                                    <h1 class="h4 text-gray-900">Bienvenido</h1>
                                    <h4 class="text-center">Restablecer contraseña</h4>
                                </div>
                                <form class="login" @submit.prevent="reset_password">
                                    <input type="hidden" v-model="token">
                                    <div class="form-floating mt-2">
                                        <input class="form-control" id="password" name="password" placeholder="Contraseña"
                                            required="" type="password" v-model="credenciales.password">
                                        <label for="InputPassword1">Contraseña</label>
                                        <span class="hasError" v-if="v$.credenciales.password.$error">
                                            {{ v$.credenciales.password.$errors[0].$message }}
                                        </span>
                                    </div>
                                    <div class="form-floating mt-2">
                                        <input class="form-control" id="password" name="password" placeholder="Contraseña"
                                            required="" type="password" v-model="credenciales.password_confirm">
                                        <label for="InputPassword1">Confirmar Contraseña</label>
                                        <span class="hasError" v-if="v$.credenciales.password_confirm.$error">
                                            {{ v$.credenciales.password_confirm.$errors[0].$message }}
                                        </span>
                                    </div>
                                    <div class="text-center mt-3">
                                        <button class="btn btn-primary" type="submit">Reiniciar contraseña</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { useUserStore } from '../../stores/user';
import * as mensajes from '../../helpers/mensajes';
import useValidate from '@vuelidate/core'
import { required, helpers, requiredUnless, email, minLength, sameAs, requiredIf } from '@vuelidate/validators'

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
            }, token: ''
        };
    },
    validations() {
        return {
            credenciales: {
                password: {
                    minLength: helpers.withMessage('La contraseña debe tener un mínimo de seis caracteres', minLength(6)),
                    containsPasswordRequirement: helpers.withMessage(
                        () => `La contraseña debe tener mínimo un caracter en mayúscula, minúscula, uno especial y un número`,
                        (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])/.test(value)
                    ),
                },
                password_confirm: {
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
        }
    },
    mounted() {
        // Obtener el valor del token de la URL
        const token = new URLSearchParams(window.location.search).get('token')
        // Asignar el valor al input correspondiente
        this.token = token
    },
}
</script>
