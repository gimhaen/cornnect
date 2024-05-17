import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SearchView from '@/views/SearchView.vue'
import MovieView from '@/views/MovieView.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: '/search/',
      name: 'SearchView',
      component: SearchView
    },
    {
      path: '/movie/',
      name: 'MovieView',
      component: MovieView
    },
    {
      path: '/Profile/',
      name: 'ProfileView',
      component: ProfileView
    }
  ]
})

export default router
