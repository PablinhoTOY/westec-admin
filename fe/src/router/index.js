import { createRouter, createWebHistory, RouterView } from 'vue-router'
import VueBodyClass from 'vue-body-class'

import Login from '../components/Auth/Login.vue'
import Registro from '../components/Auth/Registro.vue'
import ResetPassword from '../components/Auth/ResetPassword.vue'
import SendResetPassword from '../components/Auth/SendResetPassword.vue'

import PerfilUsuario from '../components/Usuario/PerfilUsuario.vue'
import DominiosUsuario from '../components/Usuario/MisDominios.vue'

import AdminGrupos from '../components/Administracion/AdministracionGrupos.vue'
import AdminUsuarios from '../components/Administracion/AdministracionUsuarios.vue'
import AdminPerRoles from '../components/Administracion/AdministracionPermisosRoles.vue'
import AdminRoles from '../components/Administracion/AdministracionRoles.vue'
import AdminPermisos from '../components/Administracion/AdministracionPermisos.vue'
import PaginaUsuario from '../components/Administracion/PaginaUsuario.vue'
import Inicio from '../components/Inicio.vue'

import PaginaPrincipal from '../components/Bienvenida/PaginaPrincipal.vue'
import TablaPrecios from '../components/Bienvenida/TablaPrecios.vue'
import PreguntasFrecuentes from '../components/Bienvenida/PreguntasFrecuentes.vue'
import Noticias from '../components/Bienvenida/Noticias.vue'
import PantallaNoticia from '../components/Noticias/PantallaNoticia.vue'
import CompraDominio from '../components/Compra/ComprarDominio.vue'
import Perfil from '../components/Administracion/AdministrarPass.vue'
import TerminosCondiciones from '../views/TerminosCondiciones.vue'
import NotFound from '../components/NotFound.vue'
import NotAccess from '../components/NotAccess.vue'
import HistorialPagos from '../components/Ingresos/HistorialPagos.vue'
import HistorialDominio from '../components/Reporte/HistorialDominio.vue'
import { useUserStore } from '../stores/user';


const all_routes = [

  {
    path: '/',
    name: 'Inicio',
    component: PaginaPrincipal
  },
  {
    path: '/precios',
    name: 'TablaPrecios',
    component: TablaPrecios
  },
  {
    path: '/FAQ',
    name: 'PreguntasFrecuentes',
    component: PreguntasFrecuentes
  },
  {
    path: '/noticias',
    name: 'Noticias',
    component: Noticias
  },
  {
    path: '/carrito',
    name: 'CompraDominio',
    component: CompraDominio,
  },
  {
    path: '/noticia/:id',
    name: 'PantallaNoticia',
    component: PantallaNoticia,
  },
  {
    path: "/login",
    name: 'Login',
    component: Login,
  },
  {
    path: "/login/Registro",
    name: 'Registro',
    component: Registro,
  },

  {
    path: "/recoverpassword/request",
    name: 'SendResetPassword',
    component: SendResetPassword,
  },
  {
    path: "/resetpassword/reset",
    name: 'ResetPassword',
    component: ResetPassword,
  },
  /* Sección de Pagos */
  {
    path: '/Administracion/Pagos',
    name: 'Historial de Pagos',
    component: HistorialPagos,
    //beforeEnter: notAuth,
    meta: {
      requirePermission: ["OIRAM23", 1]
    }
  },
  /* Sección de Dominio */
  {
    path: '/Administracion/Dominios',
    name: 'Historial Dominio',
    component: HistorialDominio,
    meta: {
      requirePermission: ["OIRAM23", 1]
    },
  },
  {
    path: "/usuario/perfil",
    name: 'PerfilUsuario',
    component: PerfilUsuario,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/usuario/misdominios",
    name: 'DominiosUsuario',
    component: DominiosUsuario,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/:catchAll(.*)',
    name: 'notFound',
    meta: { bodyClass: 'page-error' },
  },

  /*
    {
      path: '/',
      name: 'Inicio',
      component: Inicio,
    },
    */
  {
    path: '/Administracion/Usuarios',
    name: 'Administrar Usuarios',
    component: AdminUsuarios,
    beforeEnter: notAuth,
    meta: {
      requirePermission: ["OIRAM23", 1]
    }
  },
  {
    path: '/Administracion/Grupos',
    name: 'Administrar Grupos',
    component: AdminGrupos,
    beforeEnter: notAuth,
    meta: {
      requirePermission: ["RESWOB66", 1]
    }
  },
  {
    path: '/Administracion/Perfil',
    name: 'Perfil',
    component: Perfil,
    beforeEnter: notAuth,
    meta: {
      requirePermission: [1]
    }
  },
  {
    path: '/Administracion/PermisosRoles',
    name: 'Administrar Permisos y Roles',
    component: AdminPerRoles,
    beforeEnter: notAuth,
    meta: {
      requirePermission: ["KWAS935", 1]
    }
  },
  {
    path: '/Administracion/Roles',
    name: 'Administrar Roles',
    component: AdminRoles,
    beforeEnter: notAuth,
    meta: {
      requirePermission: ["DAOT54", 1]
    }
  },
  {
    path: '/Administracion/Permisos',
    name: 'Administrar Permisos',
    component: AdminPermisos,
    beforeEnter: notAuth,
    meta: {
      requirePermission: ["HCAEP32", 1]
    }
  },
  {
    path: '/Administracion/Usuarios/:id',
    name: 'PaginaUsuario',
    component: PaginaUsuario,
    beforeEnter: notAuth,
    meta: {
      requirePermission: ["OIRAM23", 1]
    }
  },
  {
    path: '/terminosycondiciones',
    name: 'Términos y Condiciones',
    component: TerminosCondiciones,
  },
  {
    path: '/403',
    component: NotAccess,
    meta: { bodyClass: 'page-error' },
  },
  {
    path: '/404',
    component: NotFound,
    meta: { bodyClass: 'page-error' },
  },
]

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: all_routes
})

router.beforeEach((to, from) => {
  const userStore = useUserStore();
  if (to.meta.requiresAuth && !userStore.isAuth) {
    return {
      name: 'Inicio',
    }
  }
})

const vueBodyClass = new VueBodyClass(all_routes)
router.beforeEach((to, from, next) => {
  vueBodyClass.guard(to, next)
  DARK_MODE.check()
})

function notAuth(to, from, next) {
  document.title = `${to.name} - Westec-PA`
  const authStore = useUserStore();

  if (authStore.isAuth) {
    const userPermissions = authStore.permisos[0].permisos
    const requiredPermissions = to.meta.requirePermission;
    const hasAccess = authStore.checkPerm(requiredPermissions, userPermissions);

    if (hasAccess)
      next();
    else
      next("/403");
  } else
    next("/login");
}