<template>
  <div class="card">
    <h2>Administración de Usuarios</h2>
    <v-tabs v-model="tab" bg-color="#7a1c79">
      <v-tab value="lista" @click="limpiarCampos()">Lista de Usuarios</v-tab>
      <v-tab value="admin" @click="desactivarupdate(), limpiarCampos()">Añadir Usuario</v-tab>
      <v-tab value="reporte" @click="limpiarCampos()">Generar Reporte</v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item value="lista" touchless>
        <v-data-table
          :headers="headers"
          :items="listaUsuarios"
          :search="search"
          :items-per-page="10"
          class="elevation-1 mt-5"
          :footer-props="{
            'items-per-page-text': 'Usuarios por página'
          }"
        >
          <template v-slot:top>
            <v-text-field
              v-model="search"
              label="Escriba aquí para filtrar los datos (cualquier columna)..."
              class="mx-4"
              prepend-inner-icon="mdi-magnify"
            ></v-text-field>
          </template>
          <template v-slot:item.active="{ item }">
            {{ item.active == true ? 'Activado' : 'Desactivado' }}
          </template>
          <template v-slot:item.roles="{ item }">
            <ul>
              <li v-for="role in item.roles" :key="role">{{ role }}</li>
            </ul>
          </template>
          <template v-slot:item.grupo_id="{ item }">
            {{ item.grupo }}
          </template>
          <template v-slot:item.accion="{ item }">
            <router-link
              :to="{
                name: 'PaginaUsuario',
                params: { id: item.id }
              }"
            >
              <v-icon title="Ver Usuario" icon="mdi-eye-circle-outline" size="large"></v-icon>
            </router-link>
            <v-btn
              class="mr-2"
              icon="mdi-pencil-outline"
              title="Editar Usuario"
              flat
              density="compact"
              color="#FFCC00"
              @click="changeTab(item)"
            ></v-btn>
            <v-btn
              class="mr-2"
              icon="mdi-delete"
              title="Eliminar Usuario"
              flat
              density="compact"
              @click="borrarUser(item.id)"
            ></v-btn>
          </template>
        </v-data-table>
      </v-window-item>
      <v-window-item value="admin" touchless>
        <br />
        <form ref="form" v-on:submit.prevent="guardarUser">
          <div class="row mb-3">
            <div class="row">
              <div class="col-md-6 col-sm-12">
                <label for="">Nombre</label>
                <input
                  type="text"
                  name="nombre"
                  id=""
                  class="form-control"
                  v-model="user.nombre"
                  required
                />
              </div>
              <div class="col-md-6 col-sm-12">
                <label for="">Apellido</label>
                <input
                  type="text"
                  name="apellido"
                  id=""
                  class="form-control"
                  v-model="user.apellido"
                  required
                />
              </div>
              <div class="col-md-6 col-sm-12">
                <label for="">Email</label>
                <input
                  type="email"
                  name="email"
                  id="email"
                  class="form-control"
                  v-model="user.email"
                  required
                />
              </div>
              <div class="col-md-6 col-sm-12">
                <label for="">Seleccionar Estado</label> <br />
                <div class="form-check form-check-inline">
                  <input
                    type="radio"
                    class="form-check-input"
                    v-model="user.active"
                    :value="true"
                    id="true"
                    required
                    name="active"
                  />
                  <label for="true" class="form-check-label mr-5"> Activado </label>
                </div>
                <div class="form-check form-check-inline">
                  <input
                    type="radio"
                    class="form-check-input"
                    v-model="user.active"
                    :value="false"
                    id="false"
                    required
                    name="active"
                  />
                  <label for="false" class="form-check-label mr-5"> Desactivado </label>
                </div>
              </div>
              <div class="col-md-6 col-sm-12">
                <label for="">Seleccionar Grupo</label>
                <select class="form-control" v-model="user.grupo_id" required>
                  <option disabled value="" selected>Seleccione uno</option>
                  <option v-for="grupo in grupos" :key="grupo.id" :value="grupo.id">
                    {{ grupo.nombre }}
                  </option>
                </select>
                <small>Agrupación general</small>
              </div>
              <!--div class="col-6">
                <label for="">Seleccionar Unidad</label>
                <select class="form-control" v-model="user.unidad_id" required>
                  <option disabled value="" selected>Seleccione uno</option>
                  <option v-for="unidad in unidades" :key="unidad.id" :value="unidad.id">
                    {{ unidad.nombre }}
                  </option>
                </select>
                <small>Unidad especifica.</small>
              </div-->
            </div>
            <div class="row">
              <div class="col">
                <label for="">Seleccionar Rol</label><br />
                <div class="form-check form-check-inline" v-for="role in roles" :key="role.id">
                  <input
                    type="checkbox"
                    class="form-check-input inline"
                    :id="role.id"
                    :value="role.name"
                    v-model="user.roles"
                  />
                  <label class="form-check-label mr-5" :for="role.id">{{ role.name }}</label>
                </div>
              </div>
            </div>
            <div class="row mt-10">
              <div class="col d-flex justify-content-around">
                <div v-if="!disableBtn">
                  <button
                    class="btn btn-warning"
                    ref="actualizarusuario"
                    @click.prevent="actualizarUser(user.id)"
                    :disabled="isBtnDisabledUpdate"
                  >
                    Actualizar Usuario
                  </button>
                </div>
                <div v-else>
                  <button
                    class="btn btn-success"
                    ref="guardarusuario"
                    :disabled="isBtnDisabledInsert"
                  >
                    Crear Usuario
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </v-window-item>

      <v-window-item value="reporte" touchless>
        <br />
        <div class="col-6">
          <label for="">Seleccionar Estado</label> <br />
          <div class="form-check form-check-inline">
            <input
              type="radio"
              class="form-check-input"
              v-model="user.active"
              v-bind:value="true"
            />
            <label for="true" class="form-check-label mr-5"> Activado </label>
          </div>
          <div class="form-check form-check-inline">
            <input
              type="radio"
              class="form-check-input"
              v-model="user.active"
              v-bind:value="false"
            />
            <label for="true" class="form-check-label mr-5"> Desactivado </label>
          </div>
        </div>
        <div class="col-6">
          <label for="">Seleccionar Grupo</label>
          <select class="form-control" v-model="user.grupo_id" required>
            <option disabled value="" selected>Seleccione uno</option>
            <option v-for="grupo in grupos" :key="grupo.id" :value="grupo.id">
              {{ grupo.nombre }}
            </option>
          </select>
        </div>
        <div class="col-6 mb-5">
          <label for="">Seleccionar Rol</label><br />
          <div class="form-check form-check-inline" v-for="role in roles" :key="role">
            <input
              type="checkbox"
              class="form-check-input inline"
              :id="role.id"
              :value="role.name"
              v-model="user.roles"
            />
            <label class="form-check-label mr-5" :for="role.name">{{ role.name }}</label>
          </div>
        </div>
        <div class="col-6">
          <label for="">Filtrar por Fecha de Creación</label> <br />
          <div class="col-3">
            <label for="">Primera Fecha:</label>
            <input
              id="fecha_creacion"
              type="date"
              name="fecha_creacion"
              v-model="user.fecha_creacion"
            />
          </div>
          <div class="col-3">
            <label for="">Segunda Fecha:</label>
            <input
              id="fecha_comparacion"
              type="date"
              name="fecha_comparacion"
              v-model="user.fecha_comparacion"
            />
          </div>
        </div>
        <button class="btn btn-success" ref="guardarusuario" @click="imprimirReporte">
          Generar Reporte
        </button>
        <br />
        <button class="btn btn-warning" @click="limpiarCampos">Reiniciar Formulario</button>
      </v-window-item>
    </v-window>
  </div>
</template>
<script>
import * as userService from '../../services/users'
import * as gruposService from '../../services/grupos'
import * as rolesService from '../../services/roles'
import * as msg from '../../helpers/mensajes'
import axios from 'axios'

import Swal from 'sweetalert2'

export default {
  name: 'AdministracióndeUsuarios',
  data() {
    return {
      errorMessage: '',
      search: '',
      headers: [
        {
          title: 'ID',
          align: 'start',
          sortable: false,
          key: 'id'
        },
        { title: 'Correo Electrónico', key: 'email' },
        { title: 'Nombre', key: 'nombre' },
        { title: 'Apellido', key: 'apellido' },
        { title: 'Estado', key: 'active' },
        { title: 'Grupo', key: 'grupo_id' },
        { title: 'Roles', key: 'roles' },
        { title: 'Fecha de Creación', key: 'fecha_creacion' },
        { title: 'Última Fecha de Login', key: 'last_login' },
        { title: 'Acciones', key: 'accion' }
      ],
      user: {
        email: '',
        nombre: '',
        apellido: '',
        active: false,
        grupo_id: [],
        roles: [],
        fecha_creacion: '',
        fecha_comparacion: '',
        unidad_id: 0
      },
      listaUsuarios: [],
      tab: null,
      grupos: [],
      unidades: [],
      disableBtn: true,
      actualizar: false
    }
  },

  computed: {
    checkedRoles() {
      return this.roles.filter((role) => role.id).map((role) => role.name)
    },

    lists() {
      return this.user.roles.join(',')
    },

    isBtnDisabledInsert() {
      return !(
        this.user.email &&
        this.user.nombre &&
        this.isEmailValid &&
        this.user.apellido &&
        this.user.grupo_id.length != 0 &&
        this.user.roles.length != 0
      )
    },
    isBtnDisabledUpdate() {
      return !(
        this.user.email &&
        this.user.nombre &&
        this.isEmailValid &&
        this.user.apellido &&
        this.user.grupo_id.length != 0 &&
        this.user.roles.length != 0
      )
    },

    isEmailValid() {
      return /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
        this.user.email
      )
      // return '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'.test(this.user.email)
    },
    /*
    computedPassMatch() {
      if (this.actualizar) {
        return true
      } else if (this.user.password != this.user.confirm) {
        return false
      } else {
        return true
      }
    },

    computedpassword_check() {
      this.has_length = /^.{13,}$/.test(this.user.password)
      this.has_number = /\d/.test(this.user.password)
      this.has_lowercase = /[a-z]/.test(this.user.password)
      this.has_uppercase = /[A-Z]/.test(this.user.password)
      this.has_special = /[!@#\$%\^\&*\)\(+=._-]/.test(this.user.password)

      if (this.actualizar) {
        return true
      } else if (
        this.has_length &&
        this.has_number &&
        this.has_lowercase &&
        this.has_uppercase &&
        this.has_special
      ) {
        return true
      }
    },
    
    */

    buttonLabel() {
      return this.showPassword ? 'Hide' : 'Show'
    }
  },

  methods: {
    /*

    passMatch() {
      if (this.user.password != this.user.confirm) {
        this.errorMessage = 'Las contraseñas no concuerdan'
        return false
      }
      this.errorMessage = ''
      return true
    },

    password_check() {
      this.has_length = /^.{13,}$/.test(this.user.password)
      this.has_number = /\d/.test(this.user.password)
      this.has_lowercase = /[a-z]/.test(this.user.password)
      this.has_uppercase = /[A-Z]/.test(this.user.password)
      this.has_special = /[!@#\$%\^\&*\)\(+=._-]/.test(this.user.password)
    },

  
    toggleShow() {
      this.showPassword = !this.showPassword
    },
      */

    validateEmail(email) {
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        return
      } else {
        alert('Email invalid!')
      }
    },

    getUsers() {
      userService
        .GetUsers()
        .then((listaUsuarios) => (this.listaUsuarios = listaUsuarios))
        .catch((err) => console.log(err))
    },

    imprimirReporte() {
      const current = new Date()
      const date = `${current.getDate()}/${current.getMonth() + 1}/${current.getFullYear()}`
      axios({
        url: import.meta.env.VITE_FLASK_APP_BASE_URL + '/users/reporte',
        //url: ApiService.get('userscsv').then(response =>  this.lista = response.data),
        method: 'POST',
        data: this.user,

        responseType: 'blob'
      })
        .then((response) => {
          var fileURL = window.URL.createObjectURL(new Blob([response.data]))

          var fileLink = document.createElement('a')

          fileLink.href = fileURL

          fileLink.setAttribute('download', 'informeusuarios_' + date + '.csv')

          document.body.appendChild(fileLink)

          fileLink.click()
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              icon: 'error',
              title: 'Oops!',
              text: 'No se encontraron resultados en su búsqueda :('
            })
          }
        })
    },

    getGrupos() {
      gruposService
        .ObtenerListadoGrupos()
        .then((listaGrupos) => (this.grupos = listaGrupos))
        .catch((err) => console.log(err))
    },
    getUnidades() {
      userService
        .GetUnidadesSIPAF()
        .then((unidades) => (this.unidades = unidades))
        .catch((err) => console.log(err))
    },
    getRoles() {
      rolesService
        .ObtenerListadoRoles()
        .then((listaRoles) => (this.roles = listaRoles))
        .catch((err) => console.log(err))
    },

    guardarUser() {
      userService.SaveUsers(this.user).then((res) => {
        msg.ShowMessages(res)
        if (res.status == 200) {
          this.getUsers()
          this.tab = 'lista'
        }
      })
    },
    actualizarUser(id) {
      userService.UpdateUsers(id, this.user).then((res) => {
        msg.ShowMessages(res)
        if (res.status == 200) {
          this.getUsers()
          this.tab = 'lista'
        }
      })
    },
    borrarUser(id) {
      Swal.fire({
        title: 'Eliminar Usuario',
        text: `Está seguro de que desea eliminar el usuario #${id}?`,
        showDenyButton: true,
        confirmButtonText: 'Eliminar',
        denyButtonText: 'Cerrar'
      }).then((result) => {
        if (result.isConfirmed) {
          msg.toastr('Eliminando, por favor espere...', 'info')
          userService
            .DeleteUsers(id)
            .then((res) => {
              msg.ShowMessages(res)
              if (res.status == 200) {
                this.getUsers()
              }
            })
            .catch((err) => console.log(err))
        }
      })
    },

    revisarcampo() {
      fecha = this.fecha_creacion.value
    },

    limpiarCampos() {
      ;(this.user = {
        email: '',
        confirm: '',
        nombre: '',
        apellido: '',
        active: '',
        grupo_id: '',
        roles: []
      }),
        (this.disableBtn = true)
    },

    desactivarupdate() {
      //  this.$refs.actualizarusuario.innerText = 'Cambio de texto'
    },

    changeTab(user) {
      this.tab = 'admin'
      this.user = user
      this.disableBtn = false
      this.actualizar = true
    }
  },

  watch: {
    email(value) {
      this.user.email = value
      this.validateEmail(value)
    }
  },

  mounted() {
    this.getUsers()
    this.getGrupos()
    this.getUnidades()
    this.getRoles()
    console.log(this.listaUsuarios)
  }
}
</script>
