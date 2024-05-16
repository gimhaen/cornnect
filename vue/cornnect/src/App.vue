<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">홈</RouterLink>
        <RouterLink to="/">검색</RouterLink>
        <RouterLink to="/">영화</RouterLink>
        <RouterLink to="/">프로필</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>

</style>
