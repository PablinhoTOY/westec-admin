<template>
    <v-card theme="dark">
        <div class="d-flex flex-no-wrap justify-space-between">
            <div class="col">
                <v-card-title>
                    Nombre: {{ nombre }}
                </v-card-title>
                <div class="d-flex">
                    <v-card-text>Fecha de entrada: {{ entrada }}</v-card-text>
                    <v-card-text>Fecha de Salida: {{ salida }}</v-card-text>
                    <v-card-text v-if="etas != 0" class="text-h5">
                        <vue-countdown :time="etas" v-slot="{ hours, minutes, seconds }">
                            {{ hours }} horas, {{ minutes }} minutos,
                            {{ seconds }} segundos.
                        </vue-countdown>
                        <span class="emojis" v-if="etas == 404">&#128284; </span>
                    </v-card-text>
                    <v-card-text class="expired" v-else>
                        Tiempo terminado &#9200;
                    </v-card-text>
                </div>
                <v-card-subtitle class="text-h6">
                    <span title="Expulsado permanentemente" class="ban" v-if="estado == 1">Expulsado Permanentemente
                        &#9940;</span>
                    <span title="Expulsado Temporalmente" class="kick" v-if="estado == 2">Expulsado Temporalmente
                        &#9203;</span>
                </v-card-subtitle>
            </div>
            <v-avatar class="ma-3" size="125" rounded="0">
                <v-img v-if="imagen" :src="imagen"></v-img>
                <v-img v-else src="/src/static/img/default_portrait.png"></v-img>
            </v-avatar>
        </div>
    </v-card>
</template>
<script>
import VueCountdown from '@chenfengyuan/vue-countdown'
export default {
    name: 'CustomCard',
    props: ['imagen', 'nombre', 'entrada', 'salida', 'etas', 'id', 'raws', 'estado'],
    components: { VueCountdown },
}
</script>