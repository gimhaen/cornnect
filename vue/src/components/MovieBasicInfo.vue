<template>
  <div>{{ movie }}</div>
  <h2>배우들</h2>
  <div v-for="(actor, index) in movie.actors" :key="index">
    <img :src="actor.profile_image" :alt="actor.name" />
    <p>{{ actor.name }}</p>
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

<style scoped></style>
