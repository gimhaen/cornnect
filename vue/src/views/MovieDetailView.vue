<template>
  <div>
    <div>
      <img
        :src="movie.detail_image"
        class="detail_image"
        alt="영화 상세 페이지"
      />
      <h1>{{ movie.title }}</h1>
    </div>
    <nav>
      <RouterLink :to="{ path: `/movie/${$route.params.tmdb_id}/review/` }"
        >리뷰</RouterLink
      >
      <RouterLink :to="{ path: `/movie/${$route.params.tmdb_id}/talk/` }"
        >무비톡</RouterLink
      >
      <RouterLink :to="{ path: `/movie/${$route.params.tmdb_id}/info/` }"
        >기본정보</RouterLink
      >
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
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
.detail_image {
  height: auto;
  width: 100%;
}

header {
  text-align: center;
}

nav {
  display: flex;
  justify-content: center;
  gap: 10px;
}
</style>
