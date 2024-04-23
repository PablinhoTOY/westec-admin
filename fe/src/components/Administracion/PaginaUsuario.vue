<template>
  <div class="card">
    <h2>Detalles del Usuario</h2>
    <div class="single-product">
      <div v-if="loaded">
        <div class="card">
          <div class="card-header">
            Información
          </div>
          <div class="card-body">
            <p>Email: {{ usuario.email }}</p>
            <p>Nombre: {{ usuario.nombre }}</p>
            <p>Apellido: {{ usuario.apellido }}</p>
            <p v-if="usuario.active == true">Estado: Activo</p>
            <p v-else-if="usuario.active == false">Estado: Desactivado</p>
            <p>Grupo: {{ usuario.grupo }}</p>
            <p>Roles: 
             <ul>
              <li v-for="role in usuario.roles" :key="role">{{ role }}</li>
            </ul>
            </p>
            <p>Fecha de Creación: {{ usuario.fecha_creacion }}</p>
            <p>Último inicio de Sesión: {{ usuario.last_login }}</p>
            <router-link :to="'/Administracion/Usuarios'" class="btn btn-primary"> Regresar </router-link>
          </div>
        </div>
      </div>
      <div v-else>
        <h3>Cargando...</h3>
      </div>
    </div>
  </div>
</template>
  
<script>

import * as userService from '../../services/users'

export default {
  name: 'PaginaUsuario',
  data() {
    return {
      usuario: {
        nombre: '',
        apellido: '',
        email: '',
        active: '',
        grupo_id: '',
        fecha_creacion: '',
        last_login: ''
      },
      estado: '',
      loaded: false
    }
  },
  
  methods: {
    GetOneUser(id = window.location.href.split('/').pop()) {
      userService
        .GetOneUser(id)
        .then((usuario) => (this.usuario = usuario[0]))
        .catch((err) => console.log(err))
      this.loaded = true
    },
  },
  mounted() {
    this.GetOneUser()
  }

}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  text-align: center;
  margin-top: 30px;
  margin-bottom: 20px;
}
</style>
  