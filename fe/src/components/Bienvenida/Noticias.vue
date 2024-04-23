<template>
    <!-- 
  <div class="d-flex flex-column justify-content-center align-center my-6">
    <h2>{{ $t("home.head") }}</h2>
    <p>{{ $t('home.head_subtext') }}</p>
  </div> -->

    <div class="mx-10 my-4">
        Ok aqui van las noticias xd
    </div>
</template>

<script>

import * as dominiosService from '../../services/dominios.js'
import { useI18n } from 'vue-i18n'
import * as msg from '../../helpers/mensajes'

export default {
    setup() {
        const { t } = useI18n()
        return { t }
    },
    data() {
        return {

        }
    },
    mounted(){
        document.getElementById('carritoId').classList.remove('d-none')
    }
}

</script>