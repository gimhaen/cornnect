<template>
  <div>
    <div v-if="filterReviews.length === 0">
      <p>No reviews found.</p>
    </div>
    <div class="movie-review-container" v-else>
      <MovieReviewItem
        v-for="(review, index) in filterReviews"
        :key="index"
        :review="review"
      />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useArticleStore } from "@/stores/article.js";
import MovieReviewItem from "@/components/MovieReviewItem.vue";

const articleStore = useArticleStore();
const router = useRouter();
const route = useRoute();

const reviews = computed(() => {
  return articleStore.reviews;
});

onMounted(() => {
  console.log("dd");
  console.log(route.params.tmdb_id);
});
const filterReviews = computed(() => {
  const filteredReviews = [...reviews.value].filter(
    (review) => review.movie.tmdb_id == route.params.tmdb_id
  );
  console.log(filteredReviews);
  return filteredReviews.sort(
    (a, b) => new Date(b.created_at) - new Date(a.created_at)
  );
});
</script>

<style>
  .movie-review-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
</style>