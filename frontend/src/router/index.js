import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/auth/Login.vue'
import SignUpView from '../views/auth/SignUp.vue'
import Profile from '../views/profile/Profile.vue'
import Results from '@/views/search/Results.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUpView
  },
  {
    path: '/@:username',
    name: 'Profile',
    component: Profile
  },{
    path: '/result',
    name: 'Results',
    component: Results
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
