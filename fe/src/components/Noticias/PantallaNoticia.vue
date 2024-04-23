<template>
    <!-- 
  <div class="d-flex flex-column justify-content-center align-center my-6">
    <h2>{{ $t("home.head") }}</h2>
    <p>{{ $t('home.head_subtext') }}</p>
  </div> -->

    <div class="mx-10 my-4">
        Noticia {{ idNoticia }}
    </div>
</template>

<script>

import * as dominiosService from '../../services/dominios.js'
import { useI18n } from 'vue-i18n'
import * as msg from '../../helpers/mensajes'
import { router } from '../../router'

export default {
    setup() {
        const { t } = useI18n()
        return { t }
    },
    data() {
        return {
            idNoticia: 0,
        }
    },
    methods: {
        inicializaciones() {
            this.idNoticia = this.$route.params.id
            document.getElementById('carritoId').classList.remove('d-none')
        },
    },
    mounted() {
        this.inicializaciones();
    }
}

</script>