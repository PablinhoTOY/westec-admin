<!-- eslint-disable vue/valid-v-slot -->
<template>
  <div class="card">
    <h2>Historial de Dominios</h2>
    
  
    <v-window v-model="tab">
      <v-window-item value="lista" touchless>
        <v-data-table
          :items-per-page="itemsPerPage"
          :headers="headers"
          :items="dominios"
          :search="search"
          item-value="name"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-text-field
              v-model="search"
              label="Escriba aquí para filtrar los datos (cualquier columna)..."
              class="mx-4"
            >
            </v-text-field>
          </template>
          <template v-slot:item.active="{ item }">
            {{ item.raw.active == true ? 'Activado' : 'Desactivado' }}
          </template>
          <template v-slot:item.dominio="{ item }">
            <ul>
              <li v-for="dominio in item.raw.dominio" :key="dominio">{{ dominio }}</li>
            </ul>
          </template>
          <template v-slot:item.dominio_id="{ item }">
            {{ item.raw.dominio }}
          </template>

        </v-data-table>

      </v-window-item>
      <v-window-item value="admin" touchless>
        <br />
        <form ref="form" v-on:submit.prevent="guardarUser">
          <div class="row mb-3">
            <div class="row">
              <div class="col-md-6 col-sm-12">
                <label for="">Nombre del dominio</label>
                <input
                  type="text"
                  name="nombre"
                  id=""
                  class="form-control"
                  v-model="dominio.nombre"
                  required
                />
              </div>
            </div>
         
          </div>
        </form>
      </v-window-item>
    </v-window>
  </div>
</template>
<script>
import CustomCard from '../Custom/CustomCard.vue'
import * as dominioService from '../../services/dominio'
import VueCountdown from '@chenfengyuan/vue-countdown'
import axios from 'axios'
import Swal from 'sweetalert2'

export default {
  components: { VueCountdown, CustomCard },
  name: 'dominioVisualizador',
  data() {
    return {
      
      tab: null,
      search: '',
      itemsPerPage: 15,
      dis: true,
      headers: [
      {
          title: 'ID',
          align: 'start',
          sortable: false,
          key: 'id'
        },  
      {
          title: 'Dominio',
          align: 'center',
          key: 'nombre'
        }
      ],
      dominios: [],
      tab: null,
      id: [],
      nombre: [],
     
    }
  },
  methods: {
  
    getAllDominios() {
      dominioService.ObtenerListadodominio().then((dominios) => (this.dominios = dominios))
        .catch((err) => console.log(err))
    },
    
   
  
    changeTab(d) {
      this.tab = 'admin2'
      this.datas = d
      this.datas.dominio = this.dominio.id
    }
  },

  mounted() {
    this.getAllDominios()
  },
  watch: {
    search(value) {
      if (this.old_desserts.length == 0) {
        this.old_desserts = this.desserts
      }
      this.desserts = this.desserts.filter((dessert) => {
        return dessert.nombre.toLowerCase().includes(value)
      })
      if (value == '') {
        this.desserts = this.old_desserts
        this.old_desserts = []
      }
    }
  }
}
</script>