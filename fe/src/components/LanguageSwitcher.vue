<template>
  <v-select class="lanswitch py-1 mx-2" v-model="selectedLocale" 
   :onchange="switchLanguage" variant="outlined" :items="infoLocales"
   item-title="text" item-value="value" :menu-icon="this.mostrarEnDrawer ? 'mdi-arrow-down-drop-circle-outline' : ''">
    <!-- <option v-for="sLocale in infoLocales" :key="`locale-${sLocale.value}`" :value="sLocale.value"
      :selected="locale === sLocale.value">
      <span v-if="sLocale == 'es'" style="background-image:url(../static/img/es.png);">🇪🇸&emsp;</span>
      <span v-else>🇺🇸&emsp;</span>
      <span>{{ t(`locale.${sLocale}`) }}</span>

    </option> -->
    <template #prepend-item>
    </template>
  
  </v-select>

</template>


<style>

</style>

<script>
import { useI18n } from 'vue-i18n'
import { useRouter } from "vue-router"
import Tr from '@/i18n/translation'
//https://lokalise.com/blog/vue-i18n/

export default {
  setup() {
    const { t, locale } = useI18n()

    const supportedLocales = Tr.supportedLocales

    return { t, locale, supportedLocales }

  },
  data() {
    return {
      selectedLocale: '',
      infoLocales: [],
    }
  },
  methods: {
    async switchLanguage(event) {
      const newLocale = event.target.value
      console.log(newLocale)
      await Tr.switchLanguage(newLocale)
      try {
        await router.replace({ params: { locale: newLocale } })
        location.reload()
      } catch (e) {
        console.log(e)
        this.$router.push("/")
      }
    }
  },
  mounted() {
    // this.infoLocales.push(
    //   { text: this.t(`locale.es`), value: 'es', image: '../static/img/es.png' },
    //   { text: this.t(`locale.en`), value: 'en', image: '../static/img/en.png' },
    //   )
    // this.selectedLocale = this.locale
  }
}
</script>