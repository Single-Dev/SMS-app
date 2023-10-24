<template>
  <!-- <Navbar :username="username" :IsAuthenticated="IsAuthenticated" @onExit="logout"/> -->
  <SideBar
  :username="username"
  :IsAuthenticated="IsAuthenticated"
  @UpdateTerm="onTermHandler"
  @onExit="logout"
   />
  <router-view @Login="Login" @Signup="Signup" :username="username" />
</template>
<script>
import axios from 'axios'
import Navbar from '@/components/navigation/nav.vue'
import SideBar from '@/components/navigation/SideBar.vue'
export default {
  components: {
    Navbar,
    SideBar
  },
  data() {
    return {
      IsAuthenticated: false,
      username: '',
      user_id: '',
      users:[],
      getting_users: false
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
        })
        .catch(error => {
          this.$router.push('/login')
        })
    },
    async Signup(email, username, password) {
      const formData = {
        email: email,
        username: username.toLowerCase(),
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
        const response = await axios.post('/api/auth/token/login/', formData)

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
    async logout() {
      try {
        await axios.post('/api/v1/token/logout/')
        axios.defaults.headers.common['Authorization'] = ''
      } catch (error) {
      } finally {
        localStorage.removeItem('token')
        this.IsAuthenticated = false
        this.$router.push('/login')
      }
    },
    async searchForUser() {
      try {
        this.users = [];
        this.getting_users = true
        const response = await axios.get(`/api/users/?search=${this.term}`)
        const profiles = await axios.get('/api/profiles/')
        response.data.forEach(e => {
          const profile = profiles.data.find(profile => profile.user === e.id);
          const user = {
            id: e.id,
            first_name: e.first_name,
            last_name: e.last_name,
            email: e.email,
            username: e.username,
            profile_photo: profile.profile_photo,
            bio: profile.bio
          }
          this.users.push(user)
          console.log(this.users);
        })
      } catch (error) {
        console.log(error.message);
      } finally {
        this.getting_users = false
      }

    },
    onTermHandler(term) {
      this.term = term
      const currentPath = this.$router.currentRoute._rawValue.href
      if (this.term.length > 3) {
        this.searchForUser()
      }
      if (currentPath != '/result' && this.term.length > 3) {
        this.$router.push('/result')
      }
    },
  },
  mounted() {
    this.beforeCrete()
    this.getMe()
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
</style>
