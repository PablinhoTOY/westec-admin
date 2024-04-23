<template>
  <div class="card">
    <h2>Administración de Roles</h2>
    <v-tabs v-model="tab" bg-color="#7a1c79">
      <v-tab value="lista" @click="limpiarCampos()">Lista de Roles</v-tab>
      <v-tab value="admin" @click="desactivarupdate()">Añadir Rol</v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item value="lista">
        <v-data-table :headers="headers" :items="listaRoles" :search="search" :items-per-page="10"
          class="elevation-1 mt-5" :footer-props="{
            'items-per-page-text': 'Roles por página'
          }">
          <template v-slot:top>
            <v-text-field v-model="search" label="Escriba aquí para filtrar los datos (cualquier columna)..." class="mx-4"
              prepend-inner-icon="mdi-magnify"></v-text-field>
          </template>
          <template v-slot:item.accion="{ item }">
            <v-btn class="mr-2" icon="mdi-pencil-outline" title="Editar Usuario" flat density="compact" color="#FFCC00"
              @click="changeTab(item)"></v-btn>
            <v-btn class="mr-2" icon="mdi-delete" title="Eliminar Rol" flat density="compact"
              @click="borrarRol(item.id)"></v-btn>
          </template>
        </v-data-table>
      </v-window-item>
      <v-window-item value="admin">
        <form ref="form" v-on:submit.prevent="guardrRol">
          <div class="row m-3">
            <div class="form-outline mb-4">
              <label for="">Nombre</label>
              <input type="text" name="name" id="" class="form-control" v-model="rol.name" required />
            </div>
            <div class="col-6 d-flex align-items-end">
              <button class="btn btn-warning btn-block" :class="{ 'd-none': disableBtn }" ref="actualizarusuario"
                @click.prevent="actualizarRol(rol.id)" :disabled="isBtnDisabled">
                Actualizar Rol
              </button>
              <button class="btn btn-success btn-block" :class="{ 'd-none': !disableBtn }" ref="guardarusuario"
                @click.prevent="guardrRol" :disabled="isBtnDisabled">
                Crear Rol
              </button>
            </div>
          </div>
        </form>
      </v-window-item>
    </v-window>
  </div>
</template>
<script>
import * as rolesService from '../../services/roles'
import * as msg from '../../helpers/mensajes'
import useValidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'

import Swal from 'sweetalert2'

export default {
  data() {
    return {
      search: '',
      headers: [
        {
          title: 'ID',
          align: 'start',
          sortable: false,
          key: 'id'
        },
        { title: 'Rol', key: 'name' },
        { title: 'Acciones', key: 'accion' }
      ],
      rol: {
        name: ''
      },
      tab: null,
      listaRoles: [],
      disableBtn: true
    }
  },
  validations() {
    return {
      rol: {
        name: { required }
      }
    }
  },
  computed: {
    isBtnDisabled() {
      return (
        !this.rol.name
      );
    },
  },
  methods: {
    getRoles() {
      rolesService
        .ObtenerListadoRoles()
        .then((listaRoles) => (this.listaRoles = listaRoles))
        .catch((err) => console.log(err))
    },

    guardrRol() {
      rolesService.SaveRol(this.rol).then((res) => {
        msg.ShowMessages(res)
        if (res.status == 200) {
          this.getRoles()
          this.tab = 'lista'
        }
      })
    },

    actualizarRol(id) {
      rolesService.UpdateRol(id, this.rol).then((res) => {
        msg.ShowMessages(res)
        if (res.status == 200) {
          this.getRoles()
          this.tab = 'lista'
        }
      })
    },

    borrarRol(id) {
      Swal.fire({
        title: 'Eliminar Rol',
        text: `¿Está seguro que desea eliminar el rol #${id}?`,
        showDenyButton: true,
        confirmButtonText: 'Eliminar',
        denyButtonText: 'Cerrar'
      }).then((result) => {
        if (result.isConfirmed) {
          msg.toastr('Eliminando, por favor espere...', 'info')
          rolesService
            .DeleteRol(id)
            .then((res) => {
              msg.ShowMessages(res)
              if (res.status == 200) {
                this.getRoles()
              }
            })
            .catch((err) => console.log(err))
        }
      })
    },
    desactivarupdate() { this.disableBtn = true },
    limpiarCampos() {
      this.rol = {
        name: ''
      }
    },

    changeTab(rol) {
      this.tab = 'admin'
      this.rol = rol
      this.disableBtn = false
    },


  },

  mounted() {
    this.getRoles()
  }
}
</script>
  