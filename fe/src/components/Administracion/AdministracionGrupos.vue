<template>
  <div class="card">
    <h2>Administración de Grupos</h2>
    <v-tabs v-model="tab" bg-color="#7a1c79">
      <v-tab value="one">Lista de Grupos</v-tab>
      <v-tab value="two">Añadir Grupo</v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item value="one">
        <v-data-table :headers="headers" :items="listaGrupos" :search="search" :items-per-page="10"
          class="elevation-1 mt-5" :footer-props="{
            'items-per-page-text': 'Grupos por página'
          }">
          <template v-slot:top>
            <v-text-field v-model="search" label="Escriba aquí para filtrar los datos (cualquier columna)..." class="mx-4"
              prepend-inner-icon="mdi-magnify"></v-text-field>
          </template>

          <template v-slot:item.accion="{ item }">
            <v-btn class="me-5" icon="mdi-pencil" density="compact" @click="editarGrupo(item.raw)"></v-btn>
            <v-btn class="bg-danger text-white" icon="mdi-trash-can-outline" density="compact"
              @click="borrarGrupo(item.raw)"></v-btn>
          </template>
        </v-data-table>
      </v-window-item>
      <v-window-item value="two">
        <form ref="form" v-on:submit.prevent="guardarGrupo">
          <div class="row mt-5">
            <div class="form-outline mb-4">
              <label>Nombre del Grupo</label>
              <input type="text" class="form-control" v-model="grupo.nombre" />
            </div>

            <div class="form-outline mb-4">
              <label>Código</label>
              <input type="number" class="form-control" min="0" step="1" v-model="grupo.codigo" />
            </div>
          </div>
          <div class="text-center">
            <button class="btn btn-primary btn-block mb-4 btn-lg" ref="guardargrupo" type="submit" @click="guardarGrupo"
              :disabled="isBtnDisabled">
              Guardar
            </button>
          </div>
        </form>
      </v-window-item>
    </v-window>
  </div>
</template>
  
<script>
import * as grupoService from '../../services/grupos'
import Swal from 'sweetalert2'

export default {
  data() {
    return {
      tab: null,
      search: '',
      listaGrupos: [],
      headers: [
        {
          title: 'Grupo #',
          align: 'start',
          sortable: false,
          key: 'id'
        },
        { title: 'Nombre', key: 'nombre' },
        { title: 'Código', key: 'codigo' },
        { title: "Boletos Asignados", key: "boletos_asignados" },
        { title: "Boletos Disponibles", key: "boletos_disponibles" },
        { title: 'Acciones', key: 'accion' }
      ],
      grupo: {
        id: '',
        nombre: '',
        codigo: ''
      },
    }
  },
  computed: {
    isBtnDisabled() {
      // comment; the shorter version proposed by Boussadjra Brahim
      // return !(this.name && this.fname && this.phn)

      return !(this.grupo.nombre && this.grupo.codigo);
    },
  },
  methods: {

    getAllGrupos() {
      grupoService.ObtenerListadoGrupos().then((data) => {
        this.listaGrupos = data
      })
    },

    guardarGrupo() {
      if (this.grupo.nombre && this.grupo.codigo) {


        grupoService.GuardarGrupo(this.grupo).then((data) => {
          if (data) {
            this.msg(data.mensaje, data.title)

            if (data.status == 200) {
              this.grupo.nombre = null
              this.grupo.codigo = 0
              this.grupo.id = null

              this.getAllGrupos()
              this.tab = 'one'
            }
          }
        })
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Hay campos vacíos.'
        })
      }


    },

    borrarGrupo(grupo) {
      if (grupo.id) {
        Swal.fire({
          title: 'Confirmar',
          text: '¿Seguro que quiere eliminar el grupo?',
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancelar',
          showCancelButton: true
        }).then((result) => {
          if (result.isConfirmed) {
            grupoService.BorrarGrupo(grupo.id).then((data) => {
              if (data) {
                this.msg(data.mensaje, data.title)
                this.getAllGrupos()
              }
            })
          }
        })
      }
    },

    editarGrupo(grupo) {
      this.grupo.nombre = grupo.nombre
      this.grupo.codigo = grupo.codigo
      this.grupo.id = grupo.id
      this.tab = 'two'
    },

    msg(contenido, titulo) {
      titulo = titulo || 'Error'

      Swal.fire({
        title: titulo,
        text: contenido,
        confirmButtonText: 'OK'
      })
    }
  },
  mounted() {
    this.getAllGrupos()
  }
}
</script>