<template>
  <div class="" style=" z-index: 10;">
    <v-tabs class="sticky-tabs" height="60" :color='colorWestec' grow>
      <v-tab to="">Registrar dominio</v-tab>
      <v-tab to="">Tabla de precios</v-tab>
      <v-tab to="">Preguntas frecuentes</v-tab>
      <v-tab to="">Noticias</v-tab>
    </v-tabs>
    <div style="height: 60px;"></div>

    <v-card color="transparent" style="z-index: 5;">
      <v-layout>
        <v-navigation-drawer expand-on-hover permanent rail width="300" elevation="16"
          @mouseenter="mostrarEnDrawer = true" @mouseleave="mostrarEnDrawer = false"
          style="height: auto; margin-top: 60px;">

          <v-card v-if="userStore.isAuth && mostrarEnDrawer" flat :color="colorWestec" class="mb-2 mr-0" rounded="0">
            <v-list class="" :class="mostrarEnDrawer ? 'mt-2' : ''">
              <v-list-item class="pl-6" :title="`${userStore.nombre} ${userStore.apellido}`"
                :subtitle="`${userStore.empresa} ${userStore.cargo ? `(${userStore.cargo})` : ''}`">
              </v-list-item>
              <v-list-item v-if="mostrarEnDrawer">
                <v-chip class="px-auto" variant="tonal" density="comfortable" size="large">{{
        userStore.email }}
                </v-chip>
              </v-list-item>
            </v-list>
            <v-divider class="mt-1 mb-0" thickness="2px" style="border-radius: 0;"></v-divider>
          </v-card>

          <v-list density="compact" nav>

            <div v-if="carritoStore.dominios.length" class="d-flex align-center justify-content-center">
              <v-badge id="carritoId" :content="carritoStore.dominios.length" color="error"
                :offset-x="mostrarEnDrawer ? '235' : '34'" :class="userStore.isAuth ? '' : 'mt-2'"
                :style="mostrarEnDrawer ? '' : 'width: 40px !important;'" rounded="circle">
                <v-btn class="menuCarrito d-flex align-center justify-content-start mb-1" variant="flat" height="40px"
                  width="240px" :color="colorWestec" @click="accionCarrito()">
                  <span v-if="mostrarEnDrawer" class="ml-5">Carrito</span>
                  <template v-if="!mostrarEnDrawer" #prepend>
                    <v-icon style="margin-left: -1px;">mdi-cart</v-icon>
                  </template>
                  <template v-else #prepend>
                    <v-icon style="margin-right: 25px; margin-left: -1px;">mdi-cart</v-icon>
                  </template>
                  <v-icon v-if="mostrarEnDrawer" style="margin-left: 65px;" class="toggleUpDown"
                    :class='{ "rotate": isShowCarrito }'>mdi-arrow-left-drop-circle-outline</v-icon>
                </v-btn>
              </v-badge>
            </div>
            <div v-else class="d-flex align-center justify-content-center">
              <v-btn height="40px" id="carritoId" class="menuCarrito d-flex align-center justify-content-start mb-1"
                :style="mostrarEnDrawer ? 'width: 240px !important;' : 'width: 40px !important;'"
                :class="userStore.isAuth ? '' : 'mt-2'" :color="colorWestec" @click="accionCarrito()">
                <span v-if="mostrarEnDrawer" class="ml-5">Carrito</span>
                <template v-if="!mostrarEnDrawer" #prepend>
                  <v-icon style="margin-left: -1px;">mdi-cart</v-icon>
                </template>
                <template v-else #prepend>
                  <v-icon style="margin-right: 25px; margin-left: -1px;">mdi-cart</v-icon>
                </template>
                <v-icon v-if="mostrarEnDrawer" style="margin-left: 65px;" class="toggleUpDown"
                  :class='{ "rotate": isShowCarrito }'>mdi-arrow-left-drop-circle-outline</v-icon>
              </v-btn>
            </div>



            <v-list-item v-if="userStore.isAuth && mostrarEnDrawer" style="font-weight: 700;"
              class="tituloNavbar my-0 pb-0 ml-4 bold">
              <v-card width="200px" variant="flat">Usuario </v-card></v-list-item>
            <v-divider v-if="userStore.isAuth" class="mt-0 my-2 mx-1"
              :class="mostrarEnDrawer && userStore.isAuth ? '' : 'mt-3'" thickness="2px"></v-divider>
            <v-list-item v-if="userStore.isAuth" :style="`color: ${colorWestec};`"
              @click="" prepend-icon="mdi-account-details-outline"
              title="Perfil" value="perfilusuario"></v-list-item>
            <v-list-item v-if="userStore.isAuth" :style="`color: ${colorWestec};`"
              @click="" prepend-icon="mdi-web-box"
              title="Mis dominios" value="misdominios"></v-list-item>

          </v-list>



          <template #append>
            <v-list density="compact" nav border="top" class="">

              <!-- <v-list-item v-if="mostrarEnDrawer" class="tituloNavbar my-0 pb-0 ml-3 bold">
                <v-card width="200px" variant="flat">
                  Lenguaje
                  <v-icon size="20px">mdi-translate</v-icon></v-card>
              </v-list-item>
              <v-divider class="mt-0 my-3 mx-1" thickness="2px"></v-divider>
              <v-select id="LanguageSwitcher" class="languageswitcher mt-2" v-model="selectedLocale" variant="outlined"
                :items="infoLocales" item-title="text" item-value="value" density="compact"
                :menu-icon="mostrarEnDrawer ? 'mdi-arrow-down-drop-circle-outline' : ''">
                <option v-for="sLocale in infoLocales" :key="`locale-${sLocale.value}`" :value="sLocale.value"
              :selected="locale === sLocale.value">
              <span v-if="sLocale == 'es'" style="background-image:url(../static/img/es.png);">🇪🇸&emsp;</span>
              <span v-else>🇺🇸&emsp;</span>
              <span>{{ t(`locale.${sLocale}`) }}</span>
              </option> 
                <template v-if="!mostrarEnDrawer" #prepend-inner>
                  <v-icon style="margin-left: -4px;">mdi-translate</v-icon>
                </template>
              </v-select> -->

              <div class="my-2 mt-4">
                <v-btn v-if="!userStore.isAuth" class="d-flex align-center justify-content-start mb-1" block
                  id="loginId" :color="colorWestec" variant="flat" height="40px"
                  to="/login">login
                  <template #prepend>
                    <v-icon style="margin-right: 25px; margin-left: -2px;">mdi-login</v-icon>
                  </template>
                </v-btn>

                <v-btn v-if="userStore.isAuth" class="d-flex align-center justify-content-start mb-1" block
                  color="#d12229" height="40px" variant="flat" @click="logout">logout
                  <template #prepend>
                    <v-icon style="margin-right: 25px;">mdi-logout</v-icon>
                  </template>
                </v-btn>
              </div>

            </v-list>
          </template>

        </v-navigation-drawer>


        <v-navigation-drawer v-model="drawerCarrito" :color="colorWestec" width="auto" ref="drawer"
          style="height: auto; margin-top: 60px;" temporary>

          <v-list class="pb-0">
            <v-list-item class="d-flex justify-content-center mt-6 m-3">
              <v-icon class="mr-12" size="70">mdi-cart-variant</v-icon>

              <v-btn class="ml-16" size="42" variant="flat" color="transparent" icon
                @click="drawerCarrito = false, isShowCarrito = false">
                <v-icon size="42">mdi-arrow-left-bold-circle-outline</v-icon></v-btn>
            </v-list-item>
          </v-list>


          <v-list class="pt-0" density="compact" width="auto" nav>
            <v-list id="listaCarritoId" class="pt-0">
              <div v-if="carritoStore.dominios.length" class="d-flex flex-column">
                <v-btn class="mx-5 mb-4" color="white" @click="irComprar()">
                  ir al carrito
                  <v-icon class="ml-2">mdi-arrow-right-thin-circle-outline</v-icon>
                </v-btn>
                <v-card v-for="(dominio, index) in carritoStore.dominios" :key="index"
                  class="d-flex flex-column align-left justify-content-start mb-2 mx-2 " hover style="border-radius: 5px; margin: 5px;
                  cursor: default; ">
                  <div class="d-flex flex-row align-center justify-content-start mb-0">
                    <v-list-item class="mx-2 my-1 mb-0" min-width="200px" max-width="600px">
                      <span class="bold" style="font-size: 19px;">{{ `${index + 1}.` }} {{ `${dominio.dominio}`
                        }}</span>

                    </v-list-item>
                    <v-spacer></v-spacer>
                    <v-btn class="mx-2 mr-5" density="compact" variant="flat" icon="mdi-close-circle-outline"
                      color="transparent" @click="borrarCarrito(dominio)"></v-btn>

                  </div>
                  <v-divider class="m-0 p-0" style="border-color: grey !important ; opacity: 0.3 !important;"></v-divider>
                  <v-table>
                  
                    <thead>
                      <tr>
                        <th class="text-left header-table">
                          Tipo
                        </th>
                        <th class="text-center header-table">
                          Años
                        </th>
                        <th class="text-center header-table">
                          Costo/Año
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr :key="index" class="">

                        <td>
                          <v-chip v-if="dominio.tipo == 'registro'" class="pb-1" variant="flat" rounded="lg" density="compact"
                            size="large" color="success" style="border-radius: 5px;">Registro</v-chip>
                          <v-chip v-else-if="dominio.tipo == 'renovacion'" class="pb-1" variant="flat" density="compact"
                            size="large" color="info">Renovación</v-chip>
                          <v-chip v-else class="pb-1" variant="flat" density="compact" size="large"
                            color="red">Error</v-chip>
                        </td>
                        {{ dominio }}
                        <td class="text-center" style="font-size: 16px;"> {{ `${dominio.years}` }}</td>
                        <td class="text-center" style="font-size: 16px;"> {{ `${(dominio.costo/dominio.years).toFixed(2)}$` }}</td>
                      </tr>
                    </tbody>
                  </v-table>
                </v-card>
              </div>
              <div v-else class="d-flex flex-column justify-content-center">
                <v-list-item>
                  <v-card color="transparent" class="text-left" flat width="250px">
                    Primero agregue dominios al carrito para poder visualizarlos, busque su dominio perfecto
                    con nosotros y comprelo!</v-card>

                  <div class="d-flex justify-content-center">

                  </div>
                </v-list-item>
              </div>
            </v-list>
          </v-list>
        </v-navigation-drawer>

      </v-layout>
    </v-card>
    <!-- <div class="region-header">
      <nav class="d-flex flex-row align-center justify-content-center py-5 px-12">
        <div id="menuAdmin" v-if="this.userStore.isAuth">
          <div class="">
            <v-btn color='#00458d' class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas"
              role="button">
              Menú<v-icon class="ml-2">mdi-menu</v-icon>
            </v-btn>
          </div>

          <div class="offcanvas offcanvas-start w-10 card" tabindex="-1" id="offcanvas" data-bs-keyboard="true"
            data-bs-backdrop="true">
            <div class="offcanvas-header">
              <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body px-0">
              <ul class="nav nav-pills flex-column" id="sidebar-menu">

                <li class="nav-item" v-if="checkPermisions(['KABRA292', 1])">
                  <router-link class="sidebar-heading" :to="Tr.i18nRoute({ name: 'Inicio' })"><i
                      class="fa-solid fa-house"></i>Inicio</router-link>
                </li>

                <li v-if="checkPermisions(['KWAS935', 1])" class="sidebar-heading mt-5">Administración</li>

                <li class="nav-item" v-if="checkPermisions(['OIRAM23', 1])">
                  <router-link to="/Administracion/Usuarios"><i class="fas fa-user-plus"></i>Usuarios</router-link>
                </li>
                <li class="nav-item" v-if="checkPermisions(['HCAEP32', 1])">
                  <router-link to="/Administracion/Permisos"><i class="fas fa-user-tag"></i>Permisos</router-link>
                </li>
                <li class="nav-item" v-if="checkPermisions(['KWAS935', 1])">
                  <router-link to="/Administracion/PermisosRoles"><i class="fas fa-user-tag"></i>Permisos por
                    Roles</router-link>
                </li>
                <li class="nav-item" v-if="checkPermisions(['DAOT54', 1])">
                  <router-link to="/Administracion/Roles"><i class="fas fa-people-line"></i>Roles</router-link>
                </li>
                <li class="nav-item" v-if="checkPermisions(['RESWOB66', 1])">
                  <router-link to="/Administracion/Grupos"><i class="fas fa-users"></i>Grupos</router-link>
                </li>

                <li class="nav-item" v-if="checkPermisions(['RESWOB66', 1])">
            <router-link to="/Reporte/HistorialDominio"><i class="fas fa-users"></i>Reporte</router-link>
          </li>
             

              </ul>
            </div>
          </div>


        </div>






        <div class="dropdown">
          <span class="dropdown-toggle" data-bs-toggle="dropdown"><img class="img-profile rounded-circle"
              src="/src/static/img/nicpa.png" height="20" /></span>
          <ul class="dropdown-menu user">

            <li v-if="userStore.isAuth">
              <a class="dropdown-item" id="btn-logout" href="/Administracion/Perfil"><i
                  class="fas fa-person fa-sm fa-fw mr-2"></i> Cambiar Contraseña</a>
            </li>

            <li v-if="userStore.isAuth">
              <a class="dropdown-item" id="btn-logout" v-on:click="logout"><i
                  class="fas fa-sign-out-alt fa-sm fa-fw mr-2"></i> Cerrar Sesión</a>
            </li>
            <li v-else>
              <a class="dropdown-item image-link" href="/login"><i class="fas fa-sign-out-alt fa-sm fa-fw mr-2"></i>
                Iniciar Sesión</a>
            </li>
          </ul>
        </div>
      </nav>
    </div> -->
    <!-- fin de sidebar -->

    <main>

      <div class="cardMain card rounded-0">

        <div style="margin-left: 55px !important;">

          <Router-view />


        </div>
      </div>
    </main>
  </div>
</template>

<style>
.toggleUpDown {
  transition: transform .2s ease-in-out !important;
}

.region-header {
  border-top: 1px solid rgba(185, 185, 185, 0.555);
  background-color: white;
}

.sticky-tabs {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: white;
  z-index: 999;
  border-bottom: 0px solid black;
  /* Adjust z-index as needed */
}

.header-table {
  font-weight: bold !important;
  cursor: default;
  height: 0px !important;
  padding-top: 5px !important;
  padding-bottom: 5px !important;
}

.menuCarrito {
  min-width: 40px !important;
}

.v-badge__badge {
  width: 13px !important;
  height: 19px !important;
  font-size: 11px !important;
}

.languageswitcher .v-input__details {
  display: none;
}

.toggleUpDown.rotate {
  transform: rotate(180deg);
}



.border-carrito {
  border: 1px black solid;
  border-radius: 2px;
  margin-top: 0.75px
}

/* hide scrollbar para firefox */
.v-navigation-drawer__content {
  overflow-y: hidden !important;
}

/* show scrollbar para firefox */
.v-navigation-drawer__content:hover {
  overflow-y: auto !important;
}
</style>

<script>
import { useUserStore } from '../stores/user'
import { useCarritoStore } from '../stores/carrito'
import * as msg from '../helpers/mensajes'
import Swal from 'sweetalert2'

export default {
  name: 'App',
  data() {
    return {
      isShowCarrito: false,
      baseUrl: window.location.origin + '/',
      sidebar: null,
      routes: [],
      mostrarEnDrawer: false,
      drawerCarrito: false,
      infoLocales: [],
      selectedLocale: '',
    }
  },
  setup() {
    const userStore = useUserStore()
    const carritoStore = useCarritoStore()
    return { userStore, carritoStore }
  },
  methods: {
    logout() {
      this.userStore.logout();
      window.location.reload();
    },
    irComprar() {
      //document.getElementById('listaCarrito').ariaExpanded = false;
      this.$router.push({ name: 'Comprar' });
      this.isShowCarrito = false;
      this.drawerCarrito = false;
    },
    borrarCarrito(dominio) {
      Swal.fire({
        title: 'Eliminar dominio',
        text: `Está seguro de que desea eliminar el dominio ${dominio.dominio}?`,
        showDenyButton: true,
        confirmButtonText: 'Eliminar',
        confirmButtonColor: this.colorWestec,
        denyButtonText: 'Cerrar',
      }).then((result) => {
        if (result.isConfirmed) {
          this.carritoStore.eliminarDominio(dominio)
          msg.toastrTime('Dominio removido', 'success')
        }
      }).catch((err) => console.log(err))
    },
    upperCaseFirstLetter(string) {
      const modString = string[0].toUpperCase() + string.slice(1)
      return modString
    },
    accionCarrito() {
      this.isShowCarrito = !this.isShowCarrito
      this.drawerCarrito = !this.drawerCarrito
    },
    async switchLanguage(selectedLocale) {
      await Tr.switchLanguage(selectedLocale)
      try {
        await this.$router.replace({ params: { locale: selectedLocale } })
        location.reload()
      } catch (e) {
        this.$router.push("/")
      }
    },
    inicializaciones() {

     
    },
  },

  mounted() {
    this.inicializaciones();
    //watcher para visualizar la variable selectedLocale, cuando cambia, cambia el idioma
  },
  beforeUnmount() {

  },


}

// document.querySelectorAll('#sidebar-special a').forEach(el => el.addEventListener('click', e => {
//   e.preventDefault(); // Evita el comportamiento predeterminado del enlace

//   if (document.querySelector('#header-bar .navbar-toggler').offsetParent !== null) {
//     let el = document.getElementById('sidebar-menu');

//     if (el) {
//       this.sidebar = this.sidebar || new bootstrap.Collapse(el);
//       this.sidebar.toggle();
//     }
//   }
//   DARK_MODE.check()
//   //setTimeout(, 20)
// }
// ));


</script>