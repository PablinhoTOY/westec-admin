<template>
  <div class="card">
    <h2>Ingresos - Historial de Pagos</h2>

    <v-window v-model="tab">
      <v-window-item value="lista">
        <v-data-table :headers="headers" :items="listFacturas" :search="search" :items-per-page="10"
          class="elevation-1 mt-5" :footer-props="{
            'items-per-page-text': 'Permisos por página'
          }">
          <template v-slot:top>
            <v-text-field v-model="search" label="Escriba aquí para filtrar los datos (cualquier columna)..." class="mx-4"
              prepend-inner-icon="mdi-magnify"></v-text-field>
          </template>
          <template v-slot:item.detalles="{ item }">
            <v-dialog width="1000">
              <template v-slot:activator="{ props }">
                <v-icon v-bind="props" color="blue">mdi-file</v-icon>


              </template>

              <template v-slot:default="{ isActive }">
                <v-card style="background-color: rgb(237, 240, 243);" class="modal-card">
                  <v-row justify="end" align="center" class="pa-4">
                    <v-btn icon @click="isActive.value = false" flat color="transparent">
                      <v-icon class="text-red text-h4">mdi-close-box</v-icon>
                    </v-btn>
                  </v-row>
                  <v-card class="receipt-number-box" style="position: absolute; top: 10px; left: 10px; padding: 10px; background-color: #00458d; font-family:Helvetica;">
                    <v-card-subtitle  class="text-white text-h7 font-weight-bold text-left">Número de Recibo: {{ item.id }}</v-card-subtitle>
                  </v-card>
                  <div style="max-height: 60vh;">
                  <div class="logo-container" style="display: flex; align-items: center; justify-content: center;">
                    
                    <img class="logo" src="/src/static/img/nicpa.png" alt="Logo" />
                    <img class="logo" src="/src/static/img/logo_utp.png" alt="Logo"  />
                  </div>
                  <v-card-title  class="text-blue-darken-4 text-h5  text-center">Westec -Panamá</v-card-title>
                  <v-card-subtitle class="text-blue-darken-4 text-h7 text-center">FUNDACIÓN TECNOLÓGICA DE PANAMÁ</v-card-subtitle>
                  <v-card-subtitle class="text-blue-darken-4 text-h7 text-center">Edificio Administrativo de la Universidad Tecnológica
                    de Panamá</v-card-subtitle>
                  <v-card-subtitle  class="text-blue-darken-4 text-h7  text-center">Avenida Ricardo J. Alfaro, Panamá, República de
                    Panamá</v-card-subtitle>
                  <v-card-subtitle class="text-blue-darken-4 text-h7 text-center">Teléfono: +507.560-3478 /
                    +507.560-3401</v-card-subtitle>
                   
                  
                 
                  
                  <v-card-text >
                          <v-row>
                            <!-- Primer v-card -->
                            <v-col cols="12" md="6">
                              <v-card style="background-color: #ECEFF1;">
                                <v-card-text>
                                  <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Hemos recibido de: {{ item.nombrecliente }}</v-card-subtitle>
                                  <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Organización: {{ item.organizacion }}</v-card-subtitle>
                                  <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Dirección: {{ item.direccion }}</v-card-subtitle>
                                  <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Correo electrónico: {{ item.correo_electronica }}</v-card-subtitle>
                                  <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Teléfono: {{ item.id }}</v-card-subtitle>
                                  <!-- Otras subtítulos aquí -->
                                </v-card-text>
                                
                              </v-card>
                            </v-col>

                            <!-- Segundo v-card -->
                            <v-col cols="12" md="6">
                              <v-card style="background-color: #ECEFF1; max-height: 100px; max-width: 300px; position: absolute; top: 40%; right: 0%;">
                                <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Fecha de Pago: {{ formatDate(item.fechapago) }}</v-card-subtitle>
                                <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Forma de Pago: {{ item.formapago }}</v-card-subtitle>
                              </v-card>
                            </v-col>
                          </v-row>
                        </v-card-text>
                        
                      </div>
                       
                         <v-data-table
                          :headers="headersModal"
                          :items="modalData"
                         
                          mobile-breakpoint="m"
                          style="height: 400px; max-height: 400px;"
                          :footer-props="{'items-per-page-text': 'Permisos por página'}"
                          :pagination="{ }" 
                          class="elevation-1 mt-5"
                        >
                        
                          <!-- Otras configuraciones del data table ... -->

                          <template v-slot:footer>
                            <!-- Contenido del footer -->
                            <v-row justify="center">
                              
                              <v-col>
                                <!-- Puedes agregar cualquier contenido aquí -->
                                <v-btn @click="cerrarModal">Cerrar Modal</v-btn>
                              </v-col>
                            </v-row>
                          </template>
                        </v-data-table>
                        
                          <v-card-subtitle class="text-blue-darken-4 mt-7 mb-4 text-h6 text-center">¡Gracias por preferir Westec -Panamá!</v-card-subtitle>
                        
                        <v-col class="text-right" cols="12" md="6">
                              <v-card style="background-color: #ECEFF1; max-height: 400px;  max-width: 500px; position: absolute; bottom: 0 ; right: 0;">
                                <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Sub Total: {{ item.monto }}</v-card-subtitle>
                                <v-card-subtitle class="text-blue-darken-5 text-h7 text-left">Total: {{ item.monto }}</v-card-subtitle>
                              </v-card>
                            </v-col>
                            
                      </v-card>
                      <v-row justify="end" class="mt-4">
                      <v-btn @click="imprimir" class="mr-2" icon small color="primary">
                        <v-icon>mdi-printer</v-icon>
                      </v-btn>

                      <!-- Botón Cerrar -->
                      <v-btn  @click="isActive.value = false" icon small color="error">
                        <v-icon>mdi-close</v-icon>
                      </v-btn>
                    </v-row>    
              </template>



            </v-dialog>
          </template>

        </v-data-table>
        
      </v-window-item>


    </v-window>


  </div>
  

</template>

<script>

import * as permisosService from '../../services/permisos'
import * as msg from '../../helpers/mensajes'
import useValidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'
import * as facturacionService from '../../services/facturacion'
import Swal from 'sweetalert2'
import axios from 'axios'
//import html2pdf from 'html2pdf.js';

export default {
  data() {
    return {
      paginaActualModal: 1,
      totalPaginasModal: 10,
      search: '',
      headers: [
        {
          title: 'Num. Recibo',
          align: 'start',
          sortable: false,
          key: 'id'
        },
        { title: 'Nombre del Cliente', key: 'nombrecliente' },
        { title: 'Organización', key: 'organizacion' },
        { title: 'Recibo FTP', key: 'ftp' },
        { title: 'Forma de Pago', key: 'formapago' },
        { title: 'Monto', key: 'monto' },
        { title: 'Fecha de pago', key: 'fechapago' },
        { title: 'Detalles', key: 'detalles' }

      ],
      headersModal: [
      { title: 'Dominio', key: '' },
      { title: 'Tipo', key: '' },
      { title: 'Años', key: '' },
      { title: 'Precio', key: '' },
      { title: 'Descuento', key: '' },
      { title: 'Monto', key: 'monto' },
    ],
      listFacturas: [],
      tab: null,
      listaingresos: [],
      disableBtn: true,
      showModal: false,
      modalData:[]
    };
    
  },

  computed: {
    isBtnDisabled() {
      // comment; the shorter version proposed by Boussadjra Brahim
      // return !(this.name && this.fname && this.phn)
      return !(this.ingresos.nombre && this.ingresos.categoria)
    }
  },

  methods: {
    imprimir() {
      // Elemento que quieres convertir a PDF
      const element = document.getElementById('tuElemento');

      // Configuración para la generación del PDF
      const options = {
        margin: 10,
        filename: 'mi_documento.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
      };

      // Genera el PDF
      html2pdf().from(element).set(options).toPdf().outputPdf().then((pdf) => {
        // En este punto, el PDF ha sido generado
        // Puedes hacer lo que quieras con el objeto pdf
        // Por ejemplo, abrirlo en una nueva ventana/tab
        const blob = new Blob([pdf], { type: 'application/pdf' });
        const url = URL.createObjectURL(blob);
        window.open(url, '_blank');
      });
    },
    
    getAllFacturass() {
      facturacionService.GetAllFacturas().then((response) => {
        this.listFacturas = response
        console.log(this.listFacturas)
      })
    },
    methods: {
      mostrarDetalles(item) {
        console.log('Item seleccionado:', item);
        this.detallesFactura = item;
        this.showModal = true;
        console.log('showModal:', this.showModal);
      },
      cerrarModal() {
        this.showModal = false;
        this.detallesFactura = null;
      },

    },

    formatDate(date) {
   
   const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
   return new Date(date).toLocaleDateString(undefined, options);
 },


  },

  mounted() {
    this.getAllFacturass()

  }
}
</script>


