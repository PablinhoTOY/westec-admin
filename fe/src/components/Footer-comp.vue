<template>
  <footer class="footer ml-0">
    <!-- Footer Links -->
    <!-- Copyright -->
    <div class="my-12" style="margin-left: 12.5%; margin-right: 7%;">
      <div class="row d-flex aling-center justify-content-center">

        <div class="col-12 col-md-3 text-left bold mb-4 bold mb-10 mb-md-0" style="margin-top: -3px;">
          <v-img class="mb-2" src="/src/static/img/nic_light.png" width="130px"></v-img>
          Somos la organización encargada de proveer los
          servicios de información y de registrar los dominios correspondientes a nuestro país ccTLD .pa
          <v-img class="mt-8" src="/src/static/img/visa_nic.svg" width="150px"></v-img>
        </div>

        <div class="col-12 col-md-3 d-flex flex-column align-start align-md-center mb-5 mb-md-0">
          <h3 class="mb-0 mr-12">Categorías</h3>
          <ul class="list-unstyled mt-0 ml-0" style="font-size: 16px; margin-right: 23px;">
            <li class="my-1"><a href="" class="nav-link nav-link-custom py-1">Nosotros</a></li>
            <li class="my-1"><a href="" class="nav-link nav-link-custom py-1 ">Nuestras políticas</a></li>
            <li class="my-1"><a @click="this.$router.push(Tr.i18nRoute({ name: 'TablaPrecios' }))" class="nav-link nav-link-custom py-1">Tabla de precios</a></li>
            <li class="my-1"><a @click="this.$router.push(Tr.i18nRoute({ name: 'PreguntasFrecuentes' }))" class="nav-link nav-link-custom py-1">Preguntas frecuentes</a></li>
          </ul>
        </div>

        <div class="col-12 col-md-3">
          <h3>Información</h3>

          <ul class="nav nav-sidebar">
            <li class="nav-item">
              <span class="nav-link px-0 py-1 font-weight-normal">
                <i class="icon-location3"></i>
                <a href="https://goo.gl/maps/sYxB5XcHSV5Nfud9A" class="nav-link nav-link-custom p-0 mb-1" target="_blank">Edificio
                  Administrativo de la Universidad Tecnológica de Panamá Ave. Ricardo J. Alfaro, Ciudad de
                  Panamá, República de Panamá.</a>
              </span>
            </li>
            <div class="col">
            <li class="nav-item">
              <span class="nav-link nav-link-custom px-0 py-1 font-weight-normal">
                <v-icon class="mr-1 mb-1" size="23">mdi-phone</v-icon>
                Teléfono <span class="ml-2">+507 560-3478</span>
              </span>
            </li>
       
            <li class="nav-item">
              <span class="nav-link nav-link-custom px-0 py-1 font-weight-normal">
                <v-icon class="mr-1 mb-1" size="23">mdi-phone</v-icon>
                Soporte Técnico <span class="ml-2">+507 560-3232</span>
              </span>
            </li>
            <li class="nav-item">
              <span class="nav-link nav-link-custom px-0 py-1 font-weight-normal">
                <v-icon class="mr-1 mb-1" size="23">mdi-clock</v-icon>
                Lunes a Viernes <span class="ml-2">8:00 am - 4:00 pm (UTC-5)</span>
              </span>
            </li>
          </div>
          </ul>
        </div>


      </div>
    </div>

    <hr class="sidebar2" />

    <div class="footer-copyright text-center bold" style="font-size: 15px;">
      Copyright © {{ new Date().getFullYear() }}
      <a href="">Westec  Panamá</a>
      Todos los derechos reservados
    </div>
    <!-- Copyright -->
  </footer>
</template>

<style>
.nav-link-custom{
  color: white;
}
.nav-link-custom:hover{
  cursor: pointer;
  color: #d12229;
  text-decoration: underline;
}
</style>

<script>
import { useI18n } from 'vue-i18n'
import Tr from "@/i18n/translation"
export default {
    setup() {
        const { t } = useI18n();
        return { t, Tr }
    },
}
</script>

