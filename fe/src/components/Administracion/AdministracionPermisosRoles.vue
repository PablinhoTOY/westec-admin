<template>
  <div class="card">
    <h2>Administración de Permisos y Roles</h2>
    <div id="permissionsTable">
      <v-row class="headerRow">
        <div class="table-responsive">
          <router-link to="/Administracion/Roles" class="btn btn-success"><i class="fas fa-user-plus"></i> Añadir
            Rol</router-link>
          <table id="tabla-otras" class="table table-hover text-center mt-5">
            <thead class="bg-dark text-light">
              <tr>
                <th>Permiso</th>
                <th v-for="role in roles" :key="role.id">
                  {{ role.name }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="permiso in permisos" :key="permiso.id">
                <td>
                  {{ permiso.nombre }}
                </td>
                <td v-for="role in roles" :key="role.id">
                  <input class="form-check-input" type="checkbox" @change="verifyCheckedRolePermiso(role, permiso)"
                    :checked="CheckUnCheckPermisosRoles(role, permiso)" />
                </td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <th :colspan="roles.length + 1">
                  <button class="btn btn-success btn-block" @click.prevent="guardarPermisosRoles">
                    Guardar
                  </button>
                </th>
              </tr>
            </tfoot>
          </table>
        </div>
      </v-row>
    </div>
  </div>
</template>

<script>
import * as rolesService from '../../services/roles'
import * as permisosService from '../../services/permisos'
import * as rolespermisosService from '../../services/permisosroles'
import * as msg from '../../helpers/mensajes'

export default {
  data() {
    return {
      search: '',
      headers: [
        {
          title: 'ID',
          align: 'start',
          sortable: false,
          key: 'id'
        }
      ],
      selectedPermissionRoles: [],
      roles: [],
      permisos: []
    }
  },

  methods: {
    guardarPermisosRoles() {
      rolespermisosService
        .SavePermisoRol(this.selectedPermissionRoles)
        .then((res) => {
          if (res.status == 200) {
            msg.toastrPermanent(res)
            this.permisos = []
            this.roles = []
            this.selectedPermissionRoles = []

            this.getRoles()
          } else {
            msg.toastr('Ocurrió un error. No se ha logrado actualizar los registros.', 'error')
          }
        })
        .catch((err) => console.log(err))
    },
    verifyCheckedRolePermiso(role, permiso) {
      if (this.selectedPermissionRoles.length == 0) {
        this.addRolePermiso(role.id, permiso.id)
      } else {
        var seleccionados = this.selectedPermissionRoles
        var addNew = false

        var roles = seleccionados.map((r) => r.role)
        if (roles.includes(role.id)) {
          addNew = false
          var r = seleccionados
            .filter((p) => {
              return p.role == role.id
            })[0];
          if (!r.permisos.includes(permiso.id)) {
            r.permisos.push(permiso.id)
          } else {
            var index = r.permisos.indexOf(permiso.id)
            r.permisos.splice(index, 1)
          }
        } else addNew = true

        this.selectedPermissionRoles = seleccionados
      }
      if (addNew) this.addRolePermiso(role.id, permiso.id)
    },
    addRolePermiso(rol, permiso) {
      var per = []
      per.push(permiso)
      this.selectedPermissionRoles.push({
        role: rol,
        permisos: per
      })
    },
    CheckUnCheckPermisosRoles(role, permiso) {
      var checked = false
      this.selectedPermissionRoles.forEach((pr) => {
        if (pr.role == role.id) {
          if (pr.permisos.includes(permiso.id)) checked = true
        }
      })
      return checked
    },
    getRoles() {
      rolesService
        .ObtenerListadoRoles()
        .then((listaRoles) => {
          this.roles = listaRoles
          this.getPermisos()
        })
        .catch((err) => console.log(err))
    },
    getPermisos() {
      permisosService
        .ObtenerListadoPermisos()
        .then((listaPermisos) => {
          this.permisos = listaPermisos
          this.getPermisosRoles()
        })
        .catch((err) => console.log(err))
    },
    getPermisosRoles() {
      rolespermisosService
        .ObtenerListadoPermisosRoles()
        .then((listaPermisos) => {
          this.selectedPermissionRoles = listaPermisos
        })
        .catch((err) => console.log(err))
    }
  },
  mounted() {
    this.getRoles()
  }
}
</script>