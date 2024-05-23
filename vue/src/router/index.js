import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import SearchView from "@/views/SearchView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
import MovieReview from "@/components/MovieReview.vue";
import MovieTalk from "@/components/MovieTalk.vue";
import MovieBasicInfo from "@/components/MovieBasicInfo.vue";
import UserView from "@/views/UserView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import { useAuthStore } from "@/stores/auth.js";
import { createApp } from "vue";
import BoxOffice from "@/components/BoxOffice.vue";
import MainWritePage from "@/components/MainWritePage.vue";

// const app = createApp({})
// app.component('BoxOffice', BoxOffice)
// app.mount('#app')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "main",
      component: MainView,
    },
    {
      path: "/search/",
      name: "search",
      component: SearchView,
    },
    {
      path: "/user",
      name: "user",
      component: UserView,
    },
    {
      path: "/box-office",
      name: "box-office",
      component: BoxOffice,
    },
    {
      path: "/review-write",
      name: "write-page",
      component: MainWritePage,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useAuthStore();
        if (store.isAuthenticated) {
          return { name: "main" };
        }
      },
    },
    {
      path: "/login",
      name: "login",
      component: LogInView,
      beforeEnter: (to, from) => {
        const store = useAuthStore();
        if (store.isAuthenticated) {
          return { name: "main" };
        }
      },
    },
    {
      path: "/movie/:tmdb_id",
      name: "MovieDetail",
      component: MovieDetailView,
      children: [
        { path: "review", component: MovieReview },
        { path: "talk", component: MovieTalk },
        { path: "info", component: MovieBasicInfo },
      ],
    },
  ],
});

// router.beforeEach((to, from) => {
//   const store = useAuthStore()
//   if (to.name != 'login' && to.name != 'signup' && !store.isAuthenticated ) {
//     return { name: 'login' }
//   }
// })

export default router;
