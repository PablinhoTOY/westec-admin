<template>
  <!-- START NAV -->
  <div>
    <template v-if="routeName !== undefined">
      <Navbar v-if="!Authpage" />
      <!-- END NAV -->
      <!-- Footer -->
      <Footerc v-if="!Authpage" />
    </template>
    <template v-if="Authpage">
      <router-view></router-view>
    </template>

  </div>

  <!-- end Footer -->
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footerc from './components/Footer-comp.vue'
import { useUserStore } from '../src/stores/user'
import { useRoute } from 'vue-router';
import { watchEffect } from 'vue';

export default {
  name: "App",
  components: {
    Navbar, Footerc
  },
  setup() {
    const userStore = useUserStore()
    const route = useRoute()
    return { userStore, route }
  },
  data() {
    return {
      baseUrl: window.location.origin + "/",
      Authpage: false,
      routeName: null,
      AuthRoutes: ['Login', 'ResetPassword', 'Registro', 'SendResetPassword'],
    };
  },

  created() {
    watchEffect(() => {
      this.routeName = this.route.name
      for (let route of this.AuthRoutes) {
        if (this.route.name == route) {
          this.Authpage = true;
          break;
        } else {
          this.Authpage = false;
        }
      }
      // if (this.route.name == 'Login' || this.route.name == 'ResetPassword' || this.route.name == 'Registro') {
      //   this.Authpage = true;
      // } else {
      //   this.Authpage = false;
      // }
    },
    )
  }
};
</script>
