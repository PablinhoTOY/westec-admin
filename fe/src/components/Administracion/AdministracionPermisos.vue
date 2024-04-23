<template>
  <div class="card">
    <h2>Administración de Permisos</h2>
    <v-tabs v-model="tab" bg-color="#7a1c79">
      <v-tab value="lista" @click="limpiarCampos()">Lista de Permisos</v-tab>
      <v-tab value="admin" @click="desactivarupdate()">Añadir Permiso</v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item value="lista">
        <v-data-table
          :headers="headers"
          :items="listaPermisos"
          :search="search"
          :items-per-page="10"
          class="elevation-1 mt-5"
          :footer-props="{
            'items-per-page-text': 'Permisos por página'
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
          <template v-slot:item.accion="{ item }">
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
              title="Eliminar Permiso"
              flat
              density="compact"
              @click="borrarPermiso(item.id)"
            ></v-btn>
          </template>
        </v-data-table>
      </v-window-item>
      <v-window-item value="admin">
        <div class="row m-3">
          <div class="col-md-6 col-sm-12">
            <label for="">Permiso</label>
            <input
              type="text"
              name="name"
              id=""
              class="form-control"
              v-model="permisos.nombre"
              required
            />
          </div>
          <div class="col-md-6 col-sm-12">
            <label for="">Categoría</label>
            <input
              type="text"
              name="name"
              id=""
              class="form-control"
              v-model="permisos.categoria"
              required
            />
          </div>
          <div class="col-md-6 col-sm-12">
            <label for="">Machine Key</label>
            <input
              type="text"
              name="key"
              id=""
              class="form-control"
              v-model="permisos.key"
              required
            />
          </div>
          <div class="col-12 d-flex justify-content-around">
            <div v-if="!disableBtn">
              <button
                class="btn btn-warning"
                ref="actualizarusuario"
                @click="actualizarPermiso(permisos.id)"
                :disabled="isBtnDisabled"
              >
                Actualizar Permiso
              </button>
            </div>
            <div v-else>
              <button
                class="btn btn-success mt-4"
                ref="guardarusuario"
                @click="guardarPermiso"
                :disabled="isBtnDisabled"
              >
                Crear Permiso
              </button>
            </div>
          </div>
        </div>
      </v-window-item>
    </v-window>
  </div>
</template>
<script>
import * as permisosService from '../../services/permisos'
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
        { title: 'Permiso', key: 'nombre' },
        { title: 'Categoría', key: 'categoria' },
        { title: 'Machine Key', key: 'key' },
        { title: 'Acciones', key: 'accion' }
      ],
      permisos: {
        nombre: '',
        categoria: '',
        key: ''
      },
      tab: null,
      listaPermisos: [],
      disableBtn: true
    }
  },

  computed: {
    isBtnDisabled() {
      // comment; the shorter version proposed by Boussadjra Brahim
      // return !(this.name && this.fname && this.phn)
      return !(this.permisos.nombre && this.permisos.categoria)
    }
  },

  methods: {
    getPermisos() {
      permisosService
        .ObtenerListadoPermisos()
        .then((listaPermisos) => (this.listaPermisos = listaPermisos))
        .catch((err) => console.log(err))
    },

    guardarPermiso() {
      permisosService.SavePermiso(this.permisos).then((res) => {
        msg.ShowMessages(res)
        if (res.status == 200) {
          this.getPermisos()
          this.tab = 'lista'
        }
      })
    },

    actualizarPermiso(id) {
      permisosService.UpdatePermiso(id, this.permisos).then((res) => {
        msg.ShowMessages(res)
        if (res.status == 200) {
          this.getPermisos()
          this.tab = 'lista'
        }
      })
    },

    borrarPermiso(id) {
      Swal.fire({
        title: 'Eliminar Permiso',
        text: `¿Está seguro que desea eliminar el permiso #${id}?`,
        showDenyButton: true,
        confirmButtonText: 'Eliminar',
        denyButtonText: 'Cerrar'
      }).then((result) => {
        if (result.isConfirmed) {
          msg.toastr('Eliminando... Por favor espere.', 'info')
          permisosService
            .DeletePermiso(id)
            .then((res) => {
              msg.ShowMessages(res)
              if (res.status == 200) {
                this.getPermisos()
              }
            })
            .catch((err) => console.log(err))
        }
      })
    },
    desactivarupdate() {},
    limpiarCampos() {
      ;(this.permisos = {
        nombre: '',
        categoria: ''
      }),
        (this.disableBtn = true)
    },

    changeTab(permisos) {
      this.tab = 'admin'
      this.permisos = permisos
      this.disableBtn = false
    }
  },

  mounted() {
    this.getPermisos()
  }
}
</script>
  