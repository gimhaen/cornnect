import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import SearchView from "@/views/SearchView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
import UserView from "@/views/UserView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import { useAuthStore } from "@/stores/auth.js";
import { createApp } from "vue";
import BoxOffice from "@/components/BoxOffice.vue";

const app = createApp({});
app.component("BoxOffice", BoxOffice);
app.mount("#app");

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
      name: "BoxOffice",
      component: BoxOffice,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useAuthStore();
        if (store.isAuthenticated) {
          return { name: "login" };
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
      path: "/movie/:id",
      name: "MovieDetail",
      component: MovieDetailView,
      children: [
        { path: "", redirect: "review" },
        { path: "review", component: Review },
        { path: "movie-talk", component: MovieTalk },
        { path: "basic-info", component: BasicInfo },
      ],
    },
  ],
});

export default router;
