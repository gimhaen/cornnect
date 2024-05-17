<template>
  <header>
    <div class="container">
      <NavView />
      <main>
        <RouterView />
        <!-- <MainView /> -->
      </main>
    </div>
  </header>

</template>

<script setup>
// import { RouterView, RouterLink } from 'vue-router'
import NavView from '@/views/NavView.vue'
import MainView from '@/views/MainView.vue'
</script>

<style scoped>
.container {
  display: flex;
}

main {
  margin-left: 130px;
  flex: 1; /* 남은 영역을 모두 차지하도록 설정 */
  padding: 0;
  border: 1px solid #ccc;
}
</style>
