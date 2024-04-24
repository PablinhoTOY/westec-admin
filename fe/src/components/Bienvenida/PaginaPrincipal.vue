<template>
  <v-scroll-y-transition>

    <div v-show="localVariables.showAnim" class="">


      <div class="hero-gradient pt-12">
        <div class="px-3 px-sm-12">

          <div v-show="localVariables.showAnim" id="logo-izq" class="d-flex flex-column">
            <img class="logo" src="/src/static/img/nicpa.png" alt="Logo" />
            <div class="titulos0">
              <h3 class="nic2 text-center">Westec  Panamá</h3>
            </div>
          </div>
          <div v-show="localVariables.showAnim" class="d-flex flex-column align-center my-1 bold text-center">
            <h3></h3>
            <p></p>
          </div>


          <form class="form-inline mt-12" onsubmit="return false;">
            <div class="w-100 d-flex flex-row flex-sm-row">
              <v-text-field label="" class="v-input-dominio-principal rounded-lg"
                variant="outlined" type="text" maxlength="63" counter :loading="domain.loadingDominio" required
                v-model="domain.buscarDominio.dominio"
                @input="domain.buscarDominio.dominio = domain.buscarDominio.dominio.toLowerCase()"
                @keydown="handleInput" @paste="handlePaste">
                <template #append>
                  <div class="d-flex justify-content-center align-center flex-column flex-sm-row">

                    <v-select class="v-select-appended" variant="outlined" density="compact"
                      :items="domain.domainTypes.tipos" v-model="domain.buscarDominio.sufijo"></v-select>
                    <v-btn class="v-btn-dominio rounded-0 rounded-te-lg rounded-be-lg" :color="colorWestec" size="x-large"
                      type="submit" @click="validarBuscarDominio(domain.buscarDominio.dominio)">
                      
                    </v-btn>
                  </div>
                </template>
              </v-text-field>
            </div>
            <v-alert v-model="domain.dominioNoValido.status" class="mb-10" prominent :color="colorWestec"
              :title="domain.dominioNoValido.titulo" border="start" closable :text="domain.dominioNoValido.info"
              density="compact"></v-alert>
          </form>
          
        </div>

      </div>

      <div class=" py-12 px-4 px-sm-16">
        <div v-if="domain.responseDominioBuscado" class="d-flex flex-row justify-content-center align-center mt-6">
          <v-col v-if="domain.responseDominioBuscado.existe">
            <v-card class="mx-auto p-2 w-sm-100 w-lg-75 w-xl-50" elevation="4"
              :title="domain.responseDominioBuscado.dominioBuscado" subtitle="Dominio no disponible">
              <template #prepend>
                <v-icon icon="mdi-web" size="x-large" color="primary"></v-icon>
              </template>
              <template #append>
                <v-icon icon="mdi-cancel" size="x-large" color="error"></v-icon>
              </template>
              <v-card-text>Desafortunadamente, este dominio no está disponible en este momento. ¡Prueba con
                otro!</v-card-text>
            </v-card>
          </v-col>

          <v-col v-else>
            <v-card class="mx-auto p-2 w-sm-100 w-lg-75 w-xl-50" elevation="4"
              :title="domain.responseDominioBuscado.dominioBuscado" subtitle="Dominio disponible">
              <template #prepend>
                <v-icon icon="mdi-web" size="x-large" color="primary"></v-icon>
              </template>
              <template #append>
                <v-icon icon="mdi-check" size="x-large" color="success"></v-icon>
              </template>
              <v-card-text>¡Enhorabuena! Este dominio está disponible. ¡Puedes proceder con el registro!</v-card-text>

              <div class="d-flex justify-content-end p-3">

                <v-btn key="get" v-if="!carritoStore.checkearDominio(domain.responseDominioBuscado.dominioBuscado)"
                  @click="eliminateDominioCarrito(domain.responseDominioBuscado)" rounded="xl" height="45"
                  variant="flat" color='error'>Quitar
                  del carrito</v-btn>
                <v-btn key="getted" v-else @click="addDominioCarrito(domain.responseDominioBuscado)" rounded="xl"
                  height="45" variant="flat" :color="colorWestec">Agregar
                  al carrito</v-btn>

              </div>
            </v-card>
          </v-col>
        </div>

        <div v-if="domain.responseDominioDemas.length > 0"
          class="d-flex flex-row justify-content-center align-center mt-6">
          <v-table class="rounded-lg border w-sm-100 w-lg-75 w-xl-50" hover>
            <thead>
              <tr>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(otherDomain, index) in domain.responseDominioDemas" :key="index" class="">
                <td class="text-center" style="font-size: 18px;"> {{ otherDomain.dominioBuscado }}</td>
                <td>
                  <v-btn v-if="otherDomain.existe" @click="console.log(otherDomain)" icon="mdi-network-pos"
                    density="comfortable" rounded="lg" color="error"></v-btn>
                  <v-btn v-else-if="!carritoStore.checkearDominio(otherDomain.dominioBuscado)"
                    @click="eliminateDominioCarrito(otherDomain)" icon="mdi-close-circle-outline" density="comfortable"
                    rounded="lg" color="error"></v-btn>
                  <v-btn v-else @click="addDominioCarrito(otherDomain)" icon="mdi-plus" density="comfortable"
                    rounded="lg" color="success"></v-btn>
                </td>
              </tr>
            </tbody>
          </v-table>
        </div>


        <v-container class="mt-6">
          <v-row>
            <v-col v-for="(card, index) in info.static_cards" :key="index" cols="12" md="4">
              <v-card v-show="localVariables.showAnim" height="300px" class="d-flex flex-column 
            justify-content-center align-center" hover style="cursor: default;">
                <div class="m-3 position-absolute top-0 start-0">
                  <h1 style="font-size: 70px;" class="ml-4 text-grey">{{ index + 1 }}</h1>
                </div>
                <v-icon size="70" :color="colorWestec" class="pb-10">{{ card.icon }}</v-icon>
                <h2 style="font-size: 18px;" class="text-center">{{ card.title }}</h2>
                <p class="px-4 text-center">{{ card.body }}</p>
              </v-card>

            </v-col>

          </v-row>
        </v-container>

        <v-carousel class="rounded-lg mt-14 d-none d-md-block" hide-delimiters cycle
          :height="localVariables.parallaxHeight">
          <template #prev="{ props }">
            <v-btn class="arrow-button" variant="elevated" :color="colorWestec" icon="mdi-chevron-left"
              @click="props.onClick"></v-btn>
          </template>
          <template #next="{ props }">
            <v-btn class="arrow-button" variant="elevated" :color="colorWestec" icon="mdi-chevron-right"
              @click="props.onClick"></v-btn>
          </template>
          <v-carousel-item v-for="(image, i) in images" :key="i" eager>

            <v-parallax :src="image.src" :scale="0.5" class="d-flex flex-row align-end">
              <v-card color="rgb(0, 0, 0, 0.4)" height="100px"
                class='text-white d-flex flex-column align-center justify-content-center'>
                <div class="d-flex">
                  <span class="typewriter text-h5">{{ image.info }}</span>
                </div>
              </v-card>
            </v-parallax>

          </v-carousel-item>
        </v-carousel>

        <!-- <v-card color="rgb(0, 0, 0, 0.5)" height="450" style="backdrop-filter: blur(1.5px);"
          class='text-white d-flex flex-column align-center justify-content-center'>
        </v-card> -->


        <v-card class="my-14" min-height="60vh" variant="flat" color="transparent">
          <div class="d-flex flex-column justify-content-center align-center text-center">
            <h2></h2>
            <p></p>
            <hr :style="`border: 2px solid ${colorWestec}; width: 25%; opacity: 100%; border-radius: 5px;`">
          </div>


          <!--PARA HACER LAS NOTICIAS ESTE ES EL COMPONENTE -->

          <v-scroll-y-transition>
            <div id="noticiasId">
              <v-container v-show="localVariables.showAnim2" class="my-4">
                <v-row>
                  <v-col v-for="(card, index) in 5" :key="index" cols="12" md="4">
                    <v-card height="300px" class="nonSelectable d-flex flex-column 
              justify-content-center align-center" hover link
                      @click="">
                      <h2 style="font-size: 18px;" class="text-center">What is Lorem Ipsum?</h2>
                      <p class="px-4 text-center">Lorem Ipsum is simply dummy text of the printing and typesetting
                        industry.
                        Lorem
                        Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer
                        took
                        a
                        galley of type and scrambled it to make a type specimen book.</p>

                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </div>
          </v-scroll-y-transition>
        </v-card>

        <v-card class="my-14" min-height="20vh" variant="flat" color="transparent">

          <div class="d-flex flex-column justify-content-center align-center text-center">
            <h2>Enlaces de Interés</h2>
            <p>A continuación se presenta un listado de enlaces de interés de diferentes instituciones relacionadas</p>
            <hr :style="`border: 2px solid ${colorWestec}; width: 25%; opacity: 100%; border-radius: 5px;`">
          </div>

          <div id="interesesId">
            <v-container v-show="localVariables.showAnim2" class="my-10">
              <v-row>
                <v-col class="d-flex justify-content-center" v-for="(image, index) in imagesInteres" :key="index"
                  cols="12" md="6" lg="4" xl="
                  2">
                  <a :href="image.link" target="_blank">
                    <v-img :src="image.src" width="250px"></v-img>
                  </a>
                </v-col>
              </v-row>
            </v-container>
          </div>

        </v-card>

      </div>

    </div>
  </v-scroll-y-transition>
</template>

<style>
.nonSelectable {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.v-btn-dominio {
  min-height: 65px;
  margin-left: 0.5px;
}

.v-select-appended {
  margin-left: -16px;
  min-height: 90px !important;
  margin-bottom: -25px;
  width: 150px;

  .v-field__input {
    font-size: 16px !important;
  }

  .v-input__details {
    display: none;
  }

  .v-field {
    border-radius: 0 !important;
  }
}

.v-input-dominio-principal {

  border-radius: 10px !important;


  .v-field {
    border-radius: 0;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;

    .v-field__input {
      font-size: 20px;
      align-self: center;
    }
  }
}

.swal2-close {
  color: grey !important;
}
</style>

<script>

import * as dominiosService from '../../services/dominios.js'
import * as msg from '../../helpers/mensajes'
import { useCarritoStore } from '../../stores/carrito'
import { watchEffect } from 'vue';

// import { useUserStore } from '../../stores/user';
export default {
  setup() {
    const carritoStore = useCarritoStore();
    return { carritoStore }
  },
  data() {
    return {
      localVariables: {
        posiNoticias: 0,
        showAnim: false,
        showAnim2: false,
        parallaxHeight: null,
      },
      domain: {
        buscarDominio: {
          dominio: '',
          sufijo: '.pa',
          dominioCompleto: '',
        },
        resBuscarDominio: [],
        dominioNoValido: {
          titulo: '',
          info: '',
          type: '',
          status: false,
        },
        loadingDominio: false,
        responseDominioBuscado: null,
        responseDominioDemas: [],
        domainTypes: {
          response: [],
          tipos: [],
        }
      },
      info: {
        static_cards: [{
          icon: 'mdi-search-web',
          title: '',
          body: '',
        },
        {
          icon: 'mdi-lead-pencil',
          title: '',
          body: '',
        },
        {
          icon: 'mdi-format-paint',
          title: '',
          body: '',
        },
        ],
      },
      images: [
        {
          id: 1,
          src: 'src/static/img/laSele.jpg',
          info: 'La selección de fútbol mayor de Panamá',
        },
        {
          id: 2,
          src: 'src/static/img/canalPanama2.jpg',
          info: 'El Canal de Panamá',
        },
        {
          id: 3,
          src: 'src/static/img/panamaLaVieja.jpg',
          info: 'Panamá la Vieja',
        }
      ],
      imagesInteres: [
        {
          link: 'https://ccnso.icann.org/en',
          src: 'src/static/img/ccnso.png',
        },
        {
          link: 'https://www.iana.org',
          src: 'src/static/img/iana.png',
        },
        {
          link: 'https://www.icann.org',
          src: 'src/static/img/icann.png',
        },
        {
          link: 'https://www.lacnic.net',
          src: 'src/static/img/lacnic.png',
        },
        {
          link: 'https://lactld.org',
          src: 'src/static/img/lactld.png',
        },
        {
          link: 'https://www.wipo.int/portal/es/',
          src: 'src/static/img/ompi.png',
        },
      ],
    }
  },

  methods: {
    getDomainTypes() {
      dominiosService
        .ObtenerTiposDominios()
        .then((response) => {
          this.domain.domainTypes.response = response
          console.log(response)
          for (let tipo of this.domain.domainTypes.response) {
            this.domain.domainTypes.tipos.push(tipo.nombre)
          }
        })
        .catch((err) => console.log(err))
    },
    async getDominio() {
      this.domain.loadingDominio = true
      this.domain.buscarDominio.dominioCompleto = this.domain.buscarDominio.dominio + this.domain.buscarDominio.sufijo
     
      this.domain.responseDominioDemas = []

      if (this.carritoStore.checkearDominio(this.domain.buscarDominio.dominioCompleto)) {
        await dominiosService
            .BuscarDominio(this.domain.buscarDominio)
            .then((response => {
              console.log(response)
              if (response.status == 200) {
                for (let x of response.payload) {
                  if (x.principal) {
                    if (this.carritoStore.checkearDominio(x.dominioBuscado)) {
                      this.domain.responseDominioBuscado = x
                    } else {
                      msg.toastrPermanent('No se puede agregar el mismo dominio dos veces', 'warning')
                      this.domain.responseDominioBuscado = null
                      break;
                    }
                  }
                  else {
                    this.domain.responseDominioDemas.push(x)
                  }
                }
                console.log(this.domain.responseDominioDemas)
                this.domain.loadingDominio = false
                this.domain.dominioNoValido.status = false
              }
              else {
                msg.ShowMessages(data)
              }
            }))
            .catch((err) => console.log(err), this.domain.loadingDominio = false)
      } else {
        msg.toastrPermanent('No se puede agregar el mismo dominio dos veces', 'warning')
        this.domain.responseDominioBuscado = null
      }
      this.domain.loadingDominio = false
    },
    validarBuscarDominio(value) {
      const allowedCharactersRegex = /^(?!-)(?!.*-$)[a-zA-Z0-9ñ-]+$/;
      if (value != '') {
        if (allowedCharactersRegex.test(value)) {
          this.getDominio();
        } else {
          this.domain.dominioNoValido.titulo = 'Caracteres especiales invalidos';
          this.domain.dominioNoValido.info = 'solo se permiten caracteres alfanumericos y el caracter "-" en medio del dominio';
          this.domain.dominioNoValido.type = 'info'
          this.domain.dominioNoValido.status = true;
        }
      }
      else {
        this.domain.dominioNoValido.titulo = 'Campo vacio';
        this.domain.dominioNoValido.info = 'Se requiere que ingrese un dominio';
        this.domain.dominioNoValido.type = 'info'
        this.domain.dominioNoValido.status = true;
      }
    },
    handleInput(event) {
      // Define a regular expression to allow only certain characters
      const allowedCharactersRegex = /^[a-zA-Z0-9ñ-]+$/;
      this.domain.dominioNoValido.status = false;
      // Check if the pressed key is allowed
      if (!allowedCharactersRegex.test(event.key)) {
        // Prevent the input if the key is not allowed
        event.preventDefault();
        // this.domain.dominioNoValido.titulo = 'Caracter no valido';
        // this.domain.dominioNoValido.info = 'Solo se aceptas caracteres alfanumericos';
        // this.domain.dominioNoValido.type = 'warning'
        // this.domain.dominioNoValido.status = true;
      }
      else if (event.altKey) {
        event.preventDefault();
        // this.domain.dominioNoValido.titulo = 'No use la tecla ALT';
        // this.domain.dominioNoValido.info = 'Esta prohibido 😀👍';
        // this.domain.dominioNoValido.type = 'warning'
        // this.domain.dominioNoValido.status = true;
      }
    },
    handlePaste(event) {
      const allowedCharactersRegex = /^[a-zA-Z0-9ñ-]+$/;
      // Get the pasted text from the clipboard
      const pastedText = (event.clipboardData || window.clipboardData).getData('text');

      // Check if the pasted text contains only allowed characters
      if (!allowedCharactersRegex.test(pastedText)) {
        event.preventDefault();
        this.domain.dominioNoValido.titulo = 'Paste invalido';
        this.domain.dominioNoValido.info = 'Su ultimo texto de portapapeles tiene caracteres invalidos';
        this.domain.dominioNoValido.type = 'warning'
        this.domain.dominioNoValido.status = true;
      }
    },
    onScroll(event) {
      if (event.target.documentElement.scrollTop >= this.localVariables.posiNoticias) {
        this.localVariables.showAnim2 = true;
      }
      else {
        this.localVariables.showAnim2 = false;
      }
    },
    async eliminateDominioCarrito(dominio) {
      const data = { dominio: dominio.dominioBuscado }
      await this.carritoStore.eliminarDominio(data)
    },
    async addDominioCarrito(dominio) {
      if (this.carritoStore.checkearDominio(dominio.dominioBuscado)) {
        await this.carritoStore.agregarDominio(dominio.dominioBuscado)
      }
      else {
        msg.toastrPermanent('No se puede agregar el mismo dominio dos veces', 'warning')
      }
    },
    inicializaciones() {
      window.addEventListener("scroll", this.onScroll)
      document.getElementById('carritoId').classList.remove('d-none')
      if (window.innerWidth > 1280) {
        this.localVariables.parallaxHeight = '700'
      }
      else {
        this.localVariables.parallaxHeight = '568'
      }

      // watchEffect(() => {
      //   const bloqueNoticias = document.getElementById('noticiasId');
      //   console.log(bloqueNoticias)
      //   console.log(bloqueNoticias.getBoundingClientRect())
      //   this.localVariables.posiNoticias = window.scrollY + bloqueNoticias.getBoundingClientRect().top
      //   console.log(this.localVariables.posiNoticias)
      // })

      this.localVariables.showAnim = true;
    },
  },
  mounted() {
    this.getDomainTypes();
    this.inicializaciones();
  },
  created() {
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.onScroll)
  },
}
</script>
