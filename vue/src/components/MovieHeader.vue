<template>
  <header>
    <img :src="movie.poster_image" alt="영화 포스터" />
    <h1>{{ movie.title }}</h1>
    <p>{{ movie.description }}</p>
  </header>
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
</style>
