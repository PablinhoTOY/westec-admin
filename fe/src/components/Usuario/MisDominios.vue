<template>
    <!-- 
  <div class="d-flex flex-column justify-content-center align-center my-6">
    <h2>{{ $t("home.head") }}</h2>
    <p>{{ $t('home.head_subtext') }}</p>
  </div> -->
    <v-fade-transition>
        <div v-if="!loading" v-show="showAnim" class="my-12 mx-16">

            <div class="mb-6">
                <v-data-table v-if="misDominios != undefined" :headers="headers" :items="misDominios" :search="search"
                    :items-per-page="10" class="border elevation-16 rounded-lg">
                    <template #top>
                        <v-card class="border-bottom rounded-b-0 px-5 pt-5 pb-1 mb-3 rounded-lg" :color="colorWestec">
                            <h5 class="bold">Mis Dominios</h5>
                            <p class="">Dominios que usted ha comprado</p>
                        </v-card>
                        <v-text-field v-model="search"
                            label="Escriba aquí para filtrar los datos (cualquier columna)..." class="mx-4 rounded-lg"
                            prepend-inner-icon="mdi-magnify"></v-text-field>
                    </template>

                    <template #item.accion="{ item }">
                        <v-btn class="mr-2" text="Renovar" flat density="comfortable" :color="colorWestec"
                            @click="console.log(item)">
                            <template #append>
                                <v-icon>mdi-file-sign</v-icon>
                            </template>
                        </v-btn>

                    </template>
                </v-data-table>
                <div v-else class="d-flex align-center justify-content-center">
                    <v-card class="text-h5 p-4 d-flex align-center justify-content-center" border width="100%">
                        <div class="w-75 bold text-center">
                            Usted actualmente no cuenta con dominios de su propiedad
                        </div>
                    </v-card>
                </div>
            </div>
        </div>
        <div v-else class="my-12 mx-16 d-flex align-center justify-content-center"
            style="height: 85vh; padding-bottom: 100px;">
            <v-progress-circular :size="200" :width="7" :color="colorWestec"
                indeterminate>cargando...</v-progress-circular>
        </div>

    </v-fade-transition>

</template>

<script>

import { useUserStore } from '../../stores/user'
import * as dominiosService from '../../services/dominios.js'
import * as msg from '../../helpers/mensajes'
import Swal from 'sweetalert2'

export default {
    setup() {
        const userStore = useUserStore()
        return { userStore }
    },
    data() {
        return {
            search: '',
            headers: [
                { title: 'Dominio', align: 'start', key: 'nombre' },
                { title: 'Tipo', key: 'dominio_tipo_info.dominio_tipo.nombre' },
                { title: 'Estado', key: 'dominio_estado.alias' },
                { title: 'Fecha de expiracion', key: 'fecha_expiracion' },
                { title: 'Acciones', sortable: false, key: 'accion' }
            ],
            misDominios: [],
            loading: true,
            showAnim: false,
        }
    },
    methods: {
        async getMisDominios() {
            let info = {
                userId: this.userStore.id_acceso
                //userId: 4624
            }
            await dominiosService
                .ObtenerDominiosUsuario(info)
                .then((response) => {
                    if (response.status == 200) {
                        this.misDominios = response.payload
                        console.log(this.misDominios)
                    }
                    else {
                        msg.ShowMessages(response)
                    }
                    this.loading = false;
                    this.showAnim = true;
                })
                .catch((err) => console.log(err))
        },
        inicializaciones() {
            document.getElementById('carritoId').classList.remove('d-none')
            console.log(this.userStore.id_acceso)
        },
    },
    mounted() {
        this.inicializaciones()
        this.getMisDominios()
    }
}

</script>