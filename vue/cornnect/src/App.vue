<template>
  <header>
    <div class="container">
      <Nav />
      <main>
        <MainView />
      </main>
    </div>
  </header>
  <!-- <RouterView /> -->
</template>

<script setup>
// import { RouterView, RouterLink } from 'vue-router'
import Nav from '@/components/Nav.vue'
import MainPageView from '@/views/MainPageView.vue'
</script>

<style scoped>
.container {
  display: flex;
}

main {
  margin-left: 130px;
  flex: 1; /* 남은 영역을 모두 차지하도록 설정 */
  padding: 20px; /* 선택 사항: 게시글 영역에 여백 추가 */
  border: 1px solid #ccc; /* 선택 사항: 게시글 영역에 테두리 추가 */
}
</style>
