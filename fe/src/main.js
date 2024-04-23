import 'bootstrap/dist/css/bootstrap.css'
import 'vuetify/styles'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import { router } from './router'
import i18n from "./i18n"
import '@mdi/font/css/materialdesignicons.css'

import piniaPluginPersistedState from "pinia-plugin-persistedstate"
import vuetify from './helpers/vuetify'
import bootstrap from 'bootstrap/dist/js/bootstrap.js'

const app = createApp(App)
const pinias = createPinia()

app.config.globalProperties.colorWestec = '#00458d'

pinias.use(piniaPluginPersistedState)
app.use(pinias)
app.use(router)
app.use(i18n)
app.use(vuetify)
app.use(bootstrap)

app.mount('#app')
