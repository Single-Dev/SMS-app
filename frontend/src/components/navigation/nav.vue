<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Anonym SMS</a>
                <button @click="toggler" class="navbar-toggler" type="button">
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarColor02">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item active">
                            <router-link class="nav-link" to="/">Home</router-link>
                        </li>
                        <li v-if="IsAuthenticated == true" class="nav-item">
                            <router-link class="nav-link" :to="'/@' + username">Profile</router-link>
                        </li>
                        <div v-else class="d-flex">
                            <li class="nav-item">
                                <router-link class="nav-link" to="/login">Login</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/sign-up">Sign Up</router-link>
                            </li>
                        </div>
                        <li v-if="IsAuthenticated == true">
                            <i class="fa-solid fa-arrow-right-from-bracket fa-sm btn btn-outline-danger p-3"
                                @click="$emit('onExit')" />
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

    </div>
</template>
<script>
export default {
    props: {
        IsAuthenticated: {
            type: Boolean,
            required: true
        },
        username: {
            type: String,
            required: true
        }
    },
    methods: {
        toggler() {
            let collapse = document.querySelector('.collapse')

            collapse.classList.toggle('show')
        }
    },
}
</script>
<style scoped>
body {
    transition: all 0.5s ease;
}
</style>