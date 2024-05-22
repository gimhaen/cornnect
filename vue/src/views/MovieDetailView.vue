<template>
  <div>
    <header>
      <img :src="movie.poster_image" alt="영화 포스터" />
      <h1>{{ movie.title }}</h1>
      <p>{{ movie.description }}</p>
    </header>
    <nav>
      <router-link :to="{ path: `/movie/${$route.params.id}/review` }"
        >리뷰</router-link
      >
      <router-link :to="{ path: `/movie/${$route.params.id}/movie-talk` }"
        >무비톡</router-link
      >
      <router-link :to="{ path: `/movie/${$route.params.id}/basic-info` }"
        >기본정보</router-link
      >
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const movie = ref({});

onMounted(() => {
  const movieId = route.params.id;
  axios
    .get(`http://127.0.0.1:8000/movies/${movieId}/`)
    .then((response) => {
      movie.value = response.data;
    })
    .catch((error) => {
      console.error("Error fetching movie details:", error);
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
