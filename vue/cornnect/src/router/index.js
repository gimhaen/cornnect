import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
<<<<<<< HEAD
import SearchView from '@/views/SearchView.vue'
import MovieView from '@/views/MovieView.vue'
import ProfileView from '@/views/ProfileView.vue'
=======
import MovieView from '@/views/MovieView.vue'
import ProfileView from '@/views/ProfileView.vue'

>>>>>>> dbb8c02f35cfa1545ac65860bf9bd142c40a6461

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
<<<<<<< HEAD
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
=======
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
      
>>>>>>> dbb8c02f35cfa1545ac65860bf9bd142c40a6461
    }
  ]
})

export default router
