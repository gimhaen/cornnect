<template>
  <header>
    <div class="container">
      <NavView />
      <main>
      </main>
      <RouterLink to="/signup">SignUp</RouterLink> 
      <RouterLink to="/login ">LogIn</RouterLink>
    </div>
  </header>
  <RouterView />
</template>

<script setup>
import { computed } from 'vue'
import { RouterView, RouterLink } from 'vue-router'
import NavView from '@/views/NavView.vue'
import { useAuthStore } from './stores/auth';
const store = useAuthStore()
const isAuthenticated = computed(() => {
  return store.isAuthenticated
})
</script>

<style scoped>
.container {
  display: flex;
}

main {
  margin-left: 130px;
  flex: 1; /* 남은 영역을 모두 차지하도록 설정 */
  padding: 0; /* 선택 사항: 게시글 영역에 여백 추가 */
  border: 1px solid #ccc; /* 선택 사항: 게시글 영역에 테두리 추가 */
}
</style>
