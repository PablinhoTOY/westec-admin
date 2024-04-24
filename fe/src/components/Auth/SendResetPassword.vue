<template>
    <div class="d-flex flex-column align-center justify-content-center marginTopBot">

        <v-card elevation="8" width="448" rounded="lg" border>
            <v-btn id="" class="ml-5 mt-5" variant="flat" size="72" rounded="circle"
                to=""><v-icon color="#5c5c5c" size="56">mdi-arrow-left-bold</v-icon></v-btn>
            <form class="px-12 pb-12 sendrequest" @submit.prevent="reset_request">
                <div class="form-floating mt-2">
                    <h3 class="text-center bold mb-6">Recuperar Contraseña</h3>
                    <v-text-field v-model="credenciales.email" class="my-8 mb-4" label="Correo"
                        :error-messages="v$.credenciales.email.$errors.map(e => e.$message)"
                        @blur="v$.credenciales.email.$touch" rounded="lg" type="email" density="comfortable"
                        prepend-inner-icon="mdi-lock-outline" variant="outlined"></v-text-field>
                </div>
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
import { useVuelidate } from '@vuelidate/core'
import { email, required, helpers } from '@vuelidate/validators'

export default {
    setup() {
        const userStore = useUserStore();

        return { userStore };
    },
    data() {
        return {
            v$: useVuelidate(),
            credenciales: {
                email: '',
            },
        };
    },
    validations() {
        return {
            credenciales: {
                email: {
                    required: helpers.withMessage('Valor requerido', required),
                    email: helpers.withMessage('El valor no es un email valido', email),
                }
            }
        }
    },
    methods: {
        reset_request() {
            if (!this.v$.$error) {
                this.userStore.reset_request(this.credenciales).then(response => {
                    mensajes.ShowMessages(response);
                    if (response.status == 200) {
                        this.$router.push('/auth/reset-password')
                    }
                })
            }
        },
    },
}
</script>