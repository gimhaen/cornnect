<template>
  <div class="main-container">
    <WriteModal />
    <div class="article-container">
      <MainList class="article-list" />
    </div>
    <InfoNav class="info-nav" />   
  </div>
</template>

<script setup>
import WriteModal from '@/components/WritePage.vue'
import MainList from '@/components/MainList.vue'
import InfoNav from '@/components/layout/InfoNav.vue'
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: space-between; /* 두 요소 간에 여백 */
  align-items: flex-start; /* 선택 사항: 상단 정렬 */
  height: 100vh; /* 화면의 100% 차지 */
}

.article-container {
  flex: 1;
  display: flex;
  justify-content: center; /* 가로로 가운데 정렬 */
}

.article-list {
  padding: 20px;
  border: 1px solid #ccc;
  max-width: 600px;
  width: 100%;
}

.info-nav {
  width: 180px;
  padding: 20px;
  border: 1px solid #ccc;
  margin-left: auto /* 우측 끝에 위치시킴 */
}

</style>

