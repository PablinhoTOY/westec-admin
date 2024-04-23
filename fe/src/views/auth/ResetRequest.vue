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
                                <form class="login" @submit.prevent="reset_request">
                                    <div class="form-floating mt-2">
                                        <input class="form-control" id="email" name="email" placeholder="Correo" required=""
                                            type="email" v-model="credenciales.email">
                                        <label for="InputPassword1">Correo</label>
                                    </div>
                                    <div class="text-center mt-3">
                                        <button class="btn btn-primary" type="submit">Enviar solicitud</button>
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
export default {
    setup() {
        const userStore = useUserStore();
        return { userStore };
    },
    data() {
        return {
            credenciales: {
                email: '',
            }
        };
    },
    methods: {
        reset_request() {
            this.userStore.reset_request(this.credenciales).then(response => {
                mensajes.ShowMessages(response);
                if (response.status == 200) {
                    this.$router.push('/')
                }
            })
        }
    },
}
</script>