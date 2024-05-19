import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import MovieView from '@/views/MovieView.vue'
import ProfileView from '@/views/UserView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import { useAuthStore } from '@/stores/auth.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/movie',
      name: 'movie',
      component: MovieView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
      
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useAuthStore()
        if (store.isAuthenticated) {
          return { name: 'main' }
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView,
      beforeEnter: (to, from) => {
        const store = useAuthStore()
        if (store.isAuthenticated) {
          return { name: 'main' }
        }
      }
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useAuthStore()
  if (to.name != 'login' && to.name != 'signup' && !store.isAuthenticated ) {
    return { name: 'login' }
  }
})

export default router
