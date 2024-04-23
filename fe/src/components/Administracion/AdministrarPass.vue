<template>
      <div class="single-product">

               <div class="card">
              <div class="card-header">
                <h2>Cambio de Contraseña</h2>
                <br/>
                En este formulario podrá modificar su contraseña.
              </div>
              <div class="card-body">
                <form ref="form" v-on:submit.prevent="actualizarPassword">
                  <input type="hidden" 
                  id="id" 
                  name="id"
                  v-model="user.id" />
                    <div class="row m-3">
                        <div class="row mb-4">
                            <div class="col-12">
                                <label for="">Contraseña Actual</label>
                                <input
                                type="password"
                                name="original"
                                class="form-control"
                                ref="original"
                                v-model="user.original"
                                autocomplete="off"
                            />

                            </div>
        <div class="col-6">
            <label for="">Contraseña</label>
            <input v-if="showPassword" type="text" class="form-control" v-model="user.password" @input="password_check" required aria-label="password"/>
            <input v-else type="password" class="form-control" v-model="user.password" @input="password_check" required aria-label="password" >
          
          <div class="input-group-append">
            <button class="btn btn-outline-secondary" @click="toggleShow" type="button"><span class="icon is-small is-right">
            <i class="fas" :class="{ 'fa-eye-slash': showPassword, 'fa-eye': !showPassword }"></i>
          </span>
            </button>
            <div class="d-inline-flex p-2 checkboxes-password">
        <p class="frmValidation" :class="{'frmValidation--passed' : has_length }"><i class="frmIcon fas" :class="has_length ? 'fa-check' : 'fa-times'"></i> Tiene 13 caracteres</p>
        <p class="frmValidation" :class="{'frmValidation--passed' :has_uppercase }"><i class="frmIcon fas" :class="has_uppercase ? 'fa-check' : 'fa-times'"></i> Tiene mayúscula</p>
        <p class="frmValidation" :class="{'frmValidation--passed' :has_lowercase }"><i class="frmIcon fas" :class="has_lowercase ? 'fa-check' : 'fa-times'"></i> Tiene minúscula</p>
        <p class="frmValidation" :class="{'frmValidation--passed' : has_number }"><i class="frmIcon fas" :class="has_number ? 'fa-check' : 'fa-times'"></i> Tiene un número</p>
        <p class="frmValidation" :class="{'frmValidation--passed' : has_special }"><i class="frmIcon fas" :class="has_special ? 'fa-check' : 'fa-times'"></i> Tiene un caracter especial</p>
        </div>
        </div>
        </div>
        <div class="col-6">
          <label for="">Repetir Contraseña</label>
          <input
            type="password"
            name="confirmar"
            class="form-control"
            v-model="user.confirmar"
            autocomplete="off"
            @input="passMatch"
          />
          <p v-if="errorMessage" style="color:red">{{ errorMessage }}</p>
        </div>
        <div class="text-center mt-3">
          <button
              class="btn btn-warning"
              @click.prevent="actualizarPassword(user.id)"
              :disabled="isDisabled"
            >
              Modificar Contraseña
            </button>
        </div>
        </div>
        </div>         
      </form>

      </div>
    </div>
  </div>
</template>

    <script>
  
  import * as userService from '../../services/users'
  import { useUserStore } from '../../stores/user'
  import * as msg from '../../helpers/mensajes'
  
  export default {
    name: 'PaginaUsuario',
    setup() {
      const userStore = useUserStore()
      return { userStore }
    },
    data () {
        return {
          actualizar: false,
          showPassword: false,
          has_length:    false,
          has_number:    false,
          has_lowercase: false,
          has_uppercase: false,
          has_special:   false,
          errorMessage: '',
          user: {
            id: this.userStore.id,
            original: '',
            password: '',
            confirmar: '',
      },
        }
      },

    computed: {
        isDisabled() {
          return !(
            this.user.original 
            && this.user.password 
            && this.user.confirmar
            && this.computedPassMatch


          );

        },

        computedPassMatch(){
        if (this.actualizar){
          return true;
            }
          else if (this.user.password != this.user.confirmar) {
                        return false;
          }
           else{
                return true;
                  }
      },

      computedpassword_check () {
      this.has_length     = /^.{13,}$/.test(this.user.password);
      this.has_number    = /\d/.test(this.user.password);
      this.has_lowercase = /[a-z]/.test(this.user.password);
      this.has_uppercase = /[A-Z]/.test(this.user.password);
      this.has_special   = /[!@#\$%\^\&*\)\(+=._-]/.test(this.user.password);
      if (this.actualizar){
          return true;
            }
        else if (this.has_length && this.has_number && this.has_lowercase && this.has_uppercase && this.has_special) {
            return true
          }
                },

      },
      methods: {

        limpiarCampos() {
       //  this.$refs.form.reset();
          this.user.original = '',
          this.user.password = '',
          this.user.confirmar = '',
          this.has_length = false;
          this.has_number = false;
          this.has_lowercase = false;
          this.has_uppercase = false;
          this.has_special   = false;
    },

        passMatch() {
                   if (this.user.password != this.user.confirmar) {
                        this.errorMessage = 'Las contraseñas no concuerdan';
                        return false;
                    }
                    this.errorMessage = '';
                    return true;

                },

    password_check () {
      this.has_length     = /^.{13,}$/.test(this.user.password);
      this.has_number    = /\d/.test(this.user.password);
      this.has_lowercase = /[a-z]/.test(this.user.password);
      this.has_uppercase = /[A-Z]/.test(this.user.password);
      this.has_special   = /[!@#\$%\^\&*\)\(+=._-]/.test(this.user.password);
                },

    toggleShow() {
      this.showPassword = !this.showPassword;
    },

    actualizarPassword(id) {
        userService.changePass(id, this.user).then((res) => {
          msg.ShowMessages(res)
          this.limpiarCampos()
        })
      
    },
  },
  mounted () {
    this.userStore.id

    }
  
    }
    </script>
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style scoped>
    h3{
      text-align: center;
      margin-top: 30px;
      margin-bottom: 20px;
    }
    </style>
    