<template>
  <div>
    <MainListItem
      v-for="(review, index) in sortedReviews"
      :key="index"
      :review="review"
    />
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { useArticleStore } from "@/stores/article.js";
import MainListItem from "@/components/MainListItem.vue";

const articleStore = useArticleStore();
const reviews = computed(() => {
  return articleStore.reviews;
});

onMounted(() => {
  // console.log('1')
  articleStore.getReviews();
});

const sortedReviews = computed(() => {
  return [...reviews.value].sort(
    (a, b) => new Date(b.created_at) - new Date(a.created_at)
  );
});
</script>

<style scoped></style>
