<template>
    <p class="text-danger">{{ camera_error }}</p>
    <qr-stream :camera="camera_mode" @decode="onDecode" @init="onInit" @click="onQrClick">
        <div style="color: red" class="carnet-frame"></div>
    </qr-stream>
</template>


<script>
import { QrStream } from 'vue3-qr-reader'

class CameraSwitcher {
    constructor() {
        this._types = ['front', 'rear', 'auto'];
        this.index = 2;
    }

    get current() {
        return this._types[this.index];
    }

    get next() {
        if (this.index+1 >= this._types.length) this.index = 0;
        else this.index++;

        return this._types[this.index];
    }

    get different() {
        if (this.index+1 >= this._types.length) return this._types[0];
        return this._types[this.index+1];
    }
}
  

export default {
    emits: ['lectura'],
    props: ['reset'],
    name: 'Camara',

    components: { QrStream },

    data() {
        let cs = new CameraSwitcher()

        return {
            camera_valid: false,
            camera_switch: cs,
            camera_error: '',
            camera_mode: cs.current,
        }
    },

    watch: {
        reset: function(new_val, old_val) {
            this.resetCamera()
        }
    },

    methods: {
        async onDecode(reader) {
            let audio = new Audio(window.location.origin + '/src/static/audio/beep.mp3')
            audio.play()
            this.$emit('lectura', reader)
        },
        onQrClick() {
            if (this.camera_valid) {
                this.camera_mode = this.camera_switch.next
            }
        },
        resetCamera() {
            this.camera_mode = this.camera_switch.different
            setTimeout(() => (this.camera_mode = this.camera_switch.current), 50)
        },
        async onInit(promise) {
            try {
                await promise
                this.camera_valid = true
            } catch (error) {
                /*
                switch (error.name) {
                    case 'NotAllowedError':
                        this.camera_error = 'ERROR: Por favor, debe darle acceso al uso de la cámara. Puede hacerlo desde el ícono de candado en la barra de información del sitio.'
                        break
                    
                    case 'NotFoundError':
                        this.camera_error = 'ERROR: No se ha encontrado ningún dispositivo de camara conectado a la PC.'
                        break
                    
                    case 'NotSupportedError':
                        this.camera_error = 'ERROR: Contexto seguro requerido (HTTPS).'
                        break
                    
                    case 'NotReadableError':
                        this.camera_error = 'ERROR: Por favor, asegúrese de que la cámara no esté siendo utilizada en otro programa. Refresque la pantalla.'
                        break
                    
                    case 'OverconstrainedError':
                        //this.camera_error = 'ERROR: la camara que ha instalado, no es compatible con nuestro sistema'
                        break
                    
                    case 'StreamApiNotSupportedError':
                        this.camera_error = 'ERROR: Su navegador no es compatible con el sistema de cámara de nuestro Sistema.'
                        break
                    
                    case 'InsecureContextError':
                        this.camera_error = 'ERROR: El acceso a la cámara solo se puede utilizar en un contexto seguro. Utilice HTTPS en vez de HTTP.'
                        break
                    
                    default:
                        this.camera_error = `Error en la camara (${error.name})`
                }
                */
            }
        },
    },
}
</script>

<style>
.stream {
  max-height: 500px;
  max-width: 500px;
  margin: auto;
}
.carnet-frame {
  border-style: solid;
  border-width: 2px;
  border-color: red;
  height: 200px;
  width: 200px;
  position: absolute;
  top: 0px;
  bottom: 0px;
  right: 0px;
  left: 0px;
  margin: auto;
}

.qr-stream-wrapper {
  height: auto !important;
}

body.fullscreen .qr-stream-wrapper {
  width: 100% !important;
  height:400px !important;
  margin-bottom:20px;
}

</style>