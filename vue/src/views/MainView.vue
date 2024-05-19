<template>
  <div class="main-container">
    <ArticleList class="article-list" />
    <InfoNav class="info-nav" />   
  </div>
</template>

<script setup>
import ArticleList from '@/components/MainList.vue'
import InfoNav from '@/components/layout/InfoNav.vue'
</script>

<style scoped>
.main-container {
  display: flex;
}

.article-list {
  flex: 1;
  padding: 20px; /* 선택 사항: 게시글 영역에 여백 추가 */
  border: 1px solid #ccc; /* 선택 사항: 게시글 영역에 테두리 추가 */
}

.info-nav {
  width: 180px;
  padding: 20px; /* 선택 사항: 게시글 영역에 여백 추가 */
  border: 1px solid #ccc; /* 선택 사항: 게시글 영역에 테두리 추가 */
}

</style>

