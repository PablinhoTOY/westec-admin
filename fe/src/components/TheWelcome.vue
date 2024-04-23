<template>
  <div class="container">
    <v-tabs align-with-title v-model="tab">
      <v-tab>Generación de Boletos </v-tab>
      <v-tab>Historial de Boletos Generados</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <div>
          <h2>Administración de Boletos</h2>
          <div class="row br-warning">
            <div class="col-6">
              <label for="">Seleccionar Grupo</label>
              <select name="" id="" class="form-control" v-model="orden.grupo">
                <option v-for="grupo in grupos" :key="grupo.id" :value="grupo.id">
                  {{ grupo.nombre }}
                </option>
              </select>
            </div>
            <div class="col-6">
              <label for="">Seleccionar Grupo</label>
              <select name="" id="" class="form-control" v-model="orden.personal">
                <option v-for="persona in personal" :key="persona.id" :value="persona.id">
                  {{ persona.name }}
                </option>
              </select>
            </div>
            <div class="col-6">
              <label for="">Boletos Disponibles Actualmente</label>
              <input type="number" name="" value="0" id="" readonly class="form-control"
                v-model="orden.boletos_actuales" />
            </div>
            <div class="col-6">
              <label for="">Boletos Nuevo a asignar</label>
              <input type="number" name="" value="0" id="" class="form-control" v-model="orden.boletos_nuevos" />
            </div>
          </div>
          <div class="row mt-5">
            <button class="btn btn-success" @click="anadirOrden">
              Anadir a la orden
            </button>
            <button class="btn btn-success mt-2" @click="guardarOrden">
              Guardar orden
            </button>
          </div>
          <hr />
          <h3>Detalle de Distribucion de Boletos</h3>
          <h4>Boletos a crear y asignar en esta orden {{ total_boletos }}</h4>
          <div class="row">
            <div class="card" v-for="odr in ordenes" :key="odr.index">
              <div class="card-header">
                Boletos de
                {{
                  grupos.filter((g) => {
                    return g.id == odr.grupo;
                  })[0].nombre
                }}
                /
                {{
                  personal.filter((p) => {
                    return p.id == odr.personal;
                  })[0].name
                }}
              </div>
              <div class="card-body">
                <h5 class="card-title">
                  Cantidad de boletos actuales: {{ odr.boletos_actuales }}
                </h5>
                <h5 class="card-title">
                  Cantidad de boletos Nuevos: {{ odr.boletos_nuevos }}
                </h5>
                <p class="card-text">Descripcion:!!!</p>
              </div>
            </div>
          </div>
        </div>
      </v-tab-item>
      <v-tab-item>
        <v-data-table :headers="headers" :items="ordenesCreadas" :search="search" :items-per-page="10"
          class="elevation-1 mt-5" :footer-props="{
            'items-per-page-text': 'Ordenes por pagina',
          }">
          <template v-slot:top>
            <v-text-field v-model="search" label="Escriba aquí para filtrar los datos (cualquier columna)..."
              class="mx-4"></v-text-field>
          </template>
          <template v-slot:item.accion="{ item }">
            <v-icon v-if="item.estatus == 1" color="#5CB85C" title="Aceptar orden" @click="aceptarOrden(item)">fas
              fa-check</v-icon>
            <v-icon v-if="item.estatus == 1" color="#DC3545" title="Eliminar orden" @click="borrarOrden(item.id)">fas
              fa-trash</v-icon>
          </template>
        </v-data-table>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>
<script>
import * as msg from "../../helpers/mensajes";
import * as ordenService from "../../services/boletos";
import * as grupoService from "../../services/grupos";

import Swal from "sweetalert2";
export default {
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Orden #",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "Descripción", value: "descripcion" },
        { text: "Fecha de Creación", value: "created_at" },
        { text: "Cantidad", value: "cantidad" },
        { text: "Asignado a ", value: "grupo_id" },
        { text: "Asignado para", value: "usuario_id" },
        { text: "Estado", value: "estatus" },
        { text: "Acciones", value: "accion" },
      ],
      ordenesCreadas: [],
      tab: null,
      grupos: [],
      personal: [
        {
          id: "1",
          name: "Martin Torrijos",
        },
        {
          id: "2",
          name: "Ricardo Martinelli",
        },
        {
          id: "3",
          name: "Juan Carlos Varela",
        },
        {
          id: "4",
          name: "Mireya Moscoso",
        },
        {
          id: "5",
          name: "Perez Balladares",
        },
        {
          id: "6",
          name: "Guillermo Endara",
        },
      ],
      total_boletos: 0,
      ordenes: [],
      orden: {
        grupo: 0,
        personal: 0,
        boletos_actuales: 0,
        boletos_nuevos: 0,
        index: 0,
      },
    };
  },
  methods: {
    anadirOrden() {
      this.orden.index = this.ordenes.length;
      if (!this.validarGrupoPersonalRepetido()) {
        this.ordenes.push(this.orden);
        msg.toastrPermanent("Orden agregada...", "success");
      } else this.actualizarOrdenExistente();
      this.contarBoletos();
      this.clearOrden();
    },
    guardarOrden() {
      ordenService
        .GuardarOrden(this.ordenes)
        .then((res) => {
          msg.ShowMessages(res);
          if (res.status == 200) {
            this.clearOrden();
            this.ordenes = [];
          }
        })
        .catch((err) => console.log(err));
    },
    aceptarOrden(orden) {
      Swal.fire({
        title: "Aceptar Orden",
        text: `Esta seguro que desea procesar la orden #${orden.id}, se crearan ${orden.cantidad} boletos`,
        showDenyButton: true,
        confirmButtonText: "Aceptar",
        denyButtonText: `Cerrar`,
      }).then((result) => {
        if (result.isConfirmed) {
          msg.toastr("Procesando, por favor espere...", "info");
          ordenService
            .AceptarOrden(orden)
            .then((res) => {
              msg.ShowMessages(res);
              if (res.status == 200) {
                this.getAllOrdenes();
              }
            })
            .catch((err) => console.log(err));
        }
      });
    },
    borrarOrden(id) {
      Swal.fire({
        title: "Eliminar Orden",
        text: `Esta seguro que desea eliminar la orden #${id}?`,
        showDenyButton: true,
        confirmButtonText: "Eliminar",
        denyButtonText: `Cerrar`,
      }).then((result) => {
        if (result.isConfirmed) {
          msg.toastr("Eliminando, por favor espere...", "info");
          ordenService
            .BorrarOrden(id)
            .then((res) => {
              msg.ShowMessages(res);
              if (res.status == 200) {
                this.getAllOrdenes();
              }
            })
            .catch((err) => console.log(err));
        }
      });
    },
    contarBoletos() {
      this.total_boletos = 0;
      this.ordenes.forEach((o) => {
        this.total_boletos += parseInt(o.boletos_nuevos);
      });
    },
    actualizarOrdenExistente() {
      msg.toastr("Orden existe, actualizando...", "info");
      this.ordenes.forEach((o) => {
        if (o.grupo == this.orden.grupo && o.personal == this.orden.personal) {
          o.boletos_nuevos =
            parseInt(o.boletos_nuevos) + parseInt(this.orden.boletos_nuevos);
          msg.toastrPermanent("Orden actualizada...", "success");
        }
      });
    },
    validarGrupoPersonalRepetido() {
      var existe = false;
      this.ordenes.forEach((o) => {
        if (o.grupo == this.orden.grupo && o.personal == this.orden.personal)
          existe = true;
      });
      return existe;
    },
    getAllOrdenes() {
      ordenService
        .ObtenerTodasOrdenes()
        .then((ordenesCreadas) => (this.ordenesCreadas = ordenesCreadas))
        .catch((err) => console.log(err));
    },
    getGruposList() {
      grupoService
        .ObtenerListadoGrupos()
        .then((grupos) => (this.grupos = grupos))
        .catch((err) => console.log(err));
    },
    clearOrden() {
      this.orden = {
        grupo: 0,
        personal: 0,
        boletos_actuales: 0,
        boletos_nuevos: 0,
        index: 0,
      };
    },
  },
  mounted() {
    this.getGruposList();
    this.getAllOrdenes();
  },
};
</script>