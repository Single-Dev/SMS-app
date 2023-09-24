<template>
  <Navbar />
  <router-view @Login="Login" @Signup="Signup" />
</template>
<script>
import axios from 'axios'
import Navbar from '@/components/navigation/nav.vue'
export default {
  components:{
    Navbar 
  },
  data() {
    return {
      IsAuthenticated: false,
      username: '',
      user_id: '',
    }
  },
  methods: {
    beforeCrete() {
      this.$store.commit('initializeStore')
      const token = this.$store.state.token
      this.IsAuthenticated = this.$store.state.IsAuthenticated
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ''
      }
    },
    getMe() {
      axios.get('/api/v1/users/me/')
        .then(response => {
          this.username = response.data.username
          this.user_id = response.data.id
          console.log(this.username);
        })
        .catch(error => {
          this.$router.push('/login')
        })
    },
    async Signup(email, username, password) {
      const formData = {
        email: email,
        username: username,
        password: password,
      }
      try {
        await axios.post('/api/v1/users/', formData)
        this.$router.push('/login')
      } catch (error) {
        alert(error.message)
      }
    },
    async Login(username, password) {
      const formData = { username: username, password: password }
      try {
        const response = await axios.post('/api/v1/token/login/', formData)

        const token = response.data.auth_token

        this.$store.commit('setToken', token)

        axios.defaults.headers.common['Authorization'] = "Token " + token

        localStorage.setItem('token', token)
        this.IsAuthenticated = true
        this.$router.push('/')
      } catch (error) {
        alert(error.message)
      }
    },
  },
  mounted() {
      this.beforeCrete()
  },
}
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
