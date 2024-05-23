<template>
  <div>
    <div v-if="filterReviews.length === 0">
      <p>No reviews found.</p>
    </div>
    <div v-else>
      <MovieReviewItem
        v-for="(review, index) in filterReviews"
        :key="index"
        :review="review"
      />
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useArticleStore } from "@/stores/article.js";
import MovieReviewItem from "@/components/MovieReviewItem.vue";

const articleStore = useArticleStore();
const router = useRouter();
const route = useRoute();

const reviews = computed(() => {
  return articleStore.reviews;
});

const filterReviews = computed(() => {
  const filteredReviews = [...reviews.value].filter(
    (review) => review.movie.tmdb_id === route.params.tmdb_id
  );
  return filteredReviews;
});
</script>
