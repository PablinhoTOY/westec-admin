<template>
</template>

<script>
import { useUserStore } from '../stores/user'
import Swal from 'sweetalert2'

export default {
    setup() {
        const userStore = useUserStore()
        return { userStore }
    },
    async mounted() {
        let token = new URLSearchParams(window.location.search)
        token = JSON.stringify(Object.fromEntries(token.entries()))
        
        let response = await fetch('https://sso.utp.ac.pa/ms/user', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: token
        })

        let user = await response.json()
        let payload = {email:user.mail, password:token}
        
        this.userStore.signIn(payload).then((response) => {
            if (parseInt(response.status) == 200) {
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Inicio de sesión exitoso.',
                    showConfirmButton: false,
                    timer: 1500
                })

                this.$router.push(response.data.route)
            }
            else {
                Swal.fire({
                    icon: 'error',
                    title: response.data.title,
                    html: response.data.mensaje,
                    timer: 1500
                })

                this.$router.push('/login')
            }
        })
    }
}
</script>