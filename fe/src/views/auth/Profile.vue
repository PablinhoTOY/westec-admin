<template>
  <div class="card" data-app>
    <div class="row d-flex justify-content-center">
      <div class="col-12">
        <div class="card p-3 py-4">
          <div class="text-center">
            <img src="https://i.imgur.com/bDLhJiP.jpg" width="100" class="rounded-circle" />
          </div>

          <div class="text-center mt-3">
            <span class="bg-secondary p-1 px-4 rounded text-white">{{
              user.role
            }}</span>
            <h5 class="mt-2 mb-0">{{ user.nombres }} {{ user.apellidos }}</h5>
            <span>{{ user.cedula }}</span>

            <div class="px-4 mt-1">
              <p class="fonts">
                {{ user.email }}
              </p>
            </div>

            <ul class="social-list">
              <li><i class="fa fa-facebook"></i></li>
              <li><i class="fa fa-dribbble"></i></li>
              <li><i class="fa fa-instagram"></i></li>
              <li><i class="fa fa-linkedin"></i></li>
              <li><i class="fa fa-google"></i></li>
            </ul>

            <div class="buttons">
              <button class="btn btn-primary px-4 ms-3 text-white" @click.prevent="dialog = true">
                Cambiar Contraseña
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Cambio de Contraseña
        </v-card-title>

        <div class="card-body">
          <div class="row">
            <div class="col-12">
              <div class="form-group">
                <label for="contra">Contraseña Anterior</label>
                <input type="password" class="form-control" id="contra" required autofocus
                  v-model="credenciales.contrasena_actual" />
              </div>
            </div>
            <div class="col-12">
              <div class="form-group">
                <label for="contra">Nueva Contraseña</label>
                <input type="password" class="form-control" id="contra" required autofocus
                  v-model="credenciales.contrasena" />
              </div>
            </div>
            <div class="col-12">
              <div class="form-group">
                <label for="contra2">Confirmar Contraseña</label>
                <input type="password" class="form-control" id="contra2" required autofocus
                  v-model="credenciales.repetir_contrasena" />
              </div>
            </div>
          </div>
        </div>
        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn class="bg-danger" text @click="dialog = false"> Cerrar </v-btn><v-btn class="bg-primary" text
            @click="cambiarContrasena()">
            Cambiar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import * as mensajes from "../../../helper/mensajes";
import * as authService from "../../services/auth";
export default {
  props: ["user"],
  data() {
    return {
      dialog: false,
      credenciales: {
        contrasena_actual: "",
        contrasena: "",
        repetir_contrasena: "",
      },
    };
  },
  methods: {
    cambiarContrasena() {
      mensajes.toastrPermanent("Cambiando contraseña, por favor espere...", "info");
      authService
        .CambiarContrasena(this.credenciales)
        .then((res) => {
          mensajes.ShowMessages(res);
          if (res.status == 200) {
            this.credenciales = {
              contrasena: "",
              repetir_contrasena: "",
            };
            this.dialog = false;
          }
        })
        .catch((err) => console.log(err));
    },
  },
  mounted() {
  },
};
</script>