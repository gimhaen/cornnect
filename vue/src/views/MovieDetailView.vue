<template>
  <div>
    <header>
      <img :src="movie.poster_image" alt="영화 포스터" />
      <h1>{{ movie.title }}</h1>
      <p>{{ movie.description }}</p>
    </header>
    <nav>
      <RouterLink :to="{ path: `/movie/${$route.params.tmdb_id}/review` }"
        >리뷰</RouterLink
      >
      <RouterLink :to="{ path: `/movie/${$route.params.tmdb_id}/movie-talk` }"
        >무비톡</RouterLink
      >
      <RouterLink :to="{ path: `/movie/${$route.params.tmdb_id}/basic-info` }"
        >기본정보</RouterLink
      >
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { useMovieStore } from "@/stores/movie.js";

const movieStore = useMovieStore();
const route = useRoute();
const movie = ref({});

onMounted(() => {
  movieStore
    .movie_detail(route.params.tmdb_id)
    .then(() => {
      movie.value = movieStore.movie;
    })
    .catch((error) => {
      console.error("Error fetching movie detail:", error);
    });
});
</script>

<style scoped>
header {
  text-align: center;
}
img {
  max-width: 200px;
}
nav {
  display: flex;
  justify-content: center;
  gap: 10px;
}
</style>
