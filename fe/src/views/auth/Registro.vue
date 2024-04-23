<template>
  <div class="card">
    <div class="card-header">Registro de Personas</div>
    <div class="card-body">
      <form method="POST" @submit.prevent="registrar" class="row">
        <div class="col-6">
          <div class="form-group">
            <label for="nombres">Nombres</label>
            <input type="text" class="form-control" id="nombres" required v-model="registro.nombre" />
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label for="apellidos">Apellidos</label>
            <input type="text" class="form-control" id="apellidos" required v-model="registro.apellido" />
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label for="cedula">Cédula</label>
            <input type="text" class="form-control" id="cedula" required v-model="registro.cedula" />
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label for="correo">Correo Electrónico</label>
            <input type="email" class="form-control" id="correo" required autofocus v-model="registro.correo" />
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label for="contra">Contraseña</label>
            <input type="password" class="form-control" id="contra" required autofocus v-model="registro.contrasena" />
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label for="contra2">Confirmar Contraseña</label>
            <input type="password" class="form-control" id="contra2" required autofocus
              v-model="registro.repetir_contrasena" />
          </div>
        </div>
        <div class="col-6">
          <v-select :items="estamentos" label="Seleccione el Estamento" outlined item-text="text" item-value="value"
            v-model="registro.estamento" required></v-select>
        </div>
        <div class="col-6">
          <v-select :items="sistemas" label="Sistemas autorizados:" outlined item-text="text" item-value="value"
            v-model="registro.sistemas" multiple chips required></v-select>
        </div>
        <div class="col-12 d-flex justify-content-center mt-5">
          <button type="submit" class="btn btn-primary btn-lg text-white">
            Registrar
          </button>
        </div>
      </form>
      <v-data-table :headers="headers" :items="usuarios" :search="search" :items-per-page="10" class="elevation-1 mt-5"
        :footer-props="{
          'items-per-page-text': 'Usuarios por pagina',
        }">
        <template v-slot:top>
          <v-text-field v-model="search" label="Escriba aquí para filtrar los datos (cualquier columna)..."
            class="mx-4"></v-text-field>
        </template>
        <template v-slot:item.role="{ item }">
          <span v-if="item.role == 1">Administrativo</span>
          <span v-else-if="item.role == 2">Docente</span>
          <span v-else-if="item.role == 3">Estudiante</span>
          <span v-else-if="item.role == 4">Investigador</span>
          <span v-else>Especial</span>
        </template>
        <template v-slot:item.active="{ item }">
          <v-icon v-if="item.active == 1" class="text-success"> mdi-check </v-icon>
          <v-icon v-else class="text-danger"> mdi-block-helper </v-icon>
        </template>
      </v-data-table>
    </div>
  </div>
</template>
<script>
import * as authService from "../../services/auth";
import * as mensajes from "../../../helper/mensajes";

export default {
  data() {
    return {
      search: "",
      estamentos: [
        { value: 1, text: "Administrativo" },
        { value: 2, text: "Docente" },
        { value: 3, text: "Estudiante" },
        { value: 4, text: "Investigador" },
      ],
      sistemas: [
        { value: 1, text: "Reserva de Aulas (SAAF)" },
        { value: 2, text: "Trabajos de Graduación (FTD)" },
        { value: 3, text: "Asistencia Estudiantes (AsE)" },
        { value: 4, text: "Actividades de Extensión (AEX)" },
      ],
      headers: [
        {
          text: "Nombre",
          align: "start",
          value: "nombres",
        },
        {
          text: "Apellido",
          align: "start",
          value: "apellidos",
        },
        { text: "Cedula", value: "cedula" },
        { text: "Correo", value: "email" },
        { text: "Rol", value: "role" },
        { text: "Activo", value: "active" },
        { text: "Acciones", value: "" },
      ],
      usuarios: [],
      registro: {
        nombre: "",
        apellido: "",
        cedula: "",
        correo: "",
        contrasena: "",
        estamento: 0,
        sistemas: [],
      },
    };
  },
  methods: {
    registrar() {
      authService
        .Registrar(this.registro)
        .then((res) => {
          mensajes.ShowMessages(res);
          if (res.status == 200) {
            //Aquí lógica de algo correcto
            this.registro = {
              nombre: "",
              apellido: "",
              cedula: "",
              correo: "",
              contrasena: "",
              estamento: 0,
              sistemas: [],
            };
          }
        })
        .catch((err) => console.log(err));
    },
    getusuarios() {
      authService
        .TodosUsuarios()
        .then((usuarios) => {
          this.usuarios = usuarios;
        })
        .catch((err) => console.log(err));
    },
  },
  mounted() {
    this.getusuarios();
  },
};
</script>