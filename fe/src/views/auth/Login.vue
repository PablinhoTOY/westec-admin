<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="row">
    <div class="col-lg-6 d-lg-block bg-login-image2"></div>
    <div class="col-lg-6">
      <div class="p-0">
        <div class="logo-div text-center">
          <a href="">
            <img class="img-fluid logo" :src="'../src/static/img/logo_utp.png'" />
          </a>
        </div>
        <div class="text-center">
          <h1 class="h4 text-gray-900">Bienvenido</h1>
          <h4 class="text-center">Inicio de sesión</h4>
        </div>

        <div class="d-grid gap-2">
          <a href="https://sso.utp.ac.pa/ms/login" class="btn btn-primary m-5">Iniciar Sesión con Microsoft 365</a>
        </div>
        <!--
        <form method="POST" class="login" @submit.prevent="login">
          <div class="form-floating">
            <input class="form-control" id="email" name="email" required="" type="email" placeholder="Correo"
              v-model="credenciales.email" />
            <label for="InputEmail1">Correo</label>
          </div>
          <div class="form-floating mt-2">

            <p>
              <a href="/reset_request" class="navbar-item is-size-5 has-text-weight-semibold">
                Reiniciar Contraseña
              </a>
            </p>
          </div>
          <div class="form-group form-check">
            <input class="form-check-input" id="rememberme" name="remember" type="checkbox" value="y" />
            <label for="remember">Recuérdame</label>
          </div>
          <div class="text-center">
            <button class="btn btn-primary" type="submit">Iniciar Sesión</button>
          </div>
        </form>
      -->
      </div>
    </div>
  </div>
</template>
<script>
import { useUserStore } from '../../stores/user'
import * as mensajes from '../../helpers/mensajes'
import Swal from 'sweetalert2'
export default {
  setup() {
    const userStore = useUserStore()
    return { userStore }
  },
  data() {
    return {
      credenciales: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async login() {
      await this.userStore.signIn(this.credenciales).then((response) => {
        if (parseInt(response.status) == 200) {
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Inicio de sesión exitoso.',
            showConfirmButton: false,
            timer: 1500
          })
          console.log(response.data)
          this.$router.push(response.data.route)
          //window.location.reload()
        }
        else {
          Swal.fire({
          icon: 'error',
          title: response.data.title,
          html: response.data.mensaje,
          timer: 1500
        })

        }
      })
    }
  },
  async mounted() {
    if (window.localStorage.user) {
      await this.userStore.logout()
      window.location.reload()
    }
    
    document.body.classList.add('bg-login')
  },
  unmounted() {
    document.body.classList.remove('bg-login')
  }
}
</script>