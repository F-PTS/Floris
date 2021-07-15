import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import howWorks from '../views/howWorks.vue'
import whyBother from '../views/whyBother.vue'
import Login from '../views/Login.vue'
import register from '../views/register.vue'
import codeVer from '../views/codeVerification.vue'
import greetingPage from '../views/greetingPage.vue'
import workspace from '../views/workspace.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/how-it-works',
    name: 'HowItWorks',
    component:  howWorks 
  },
  {
    path: '/why-bother',
    name: 'whyBother',
    component:  whyBother 
  },
  {
    path: '/log-in',
    name: 'Login',
    component:  Login 
  },
  {
    path: '/register',
    name: 'Register',
    component:  register
  },
  {
    path: '/code-verification',
    name: 'codeVerification',
    component:  codeVer
  },
  {
    path: '/greeting-page',
    name: 'greetingPage',
    component: greetingPage
  },
  {
    path: '/workspace',
    name: 'workspace',
    component: workspace
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
