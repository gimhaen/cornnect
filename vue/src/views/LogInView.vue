<template>
    <div>
      <h1>로그인 페이지</h1>
      <AuthForm />
      <p>회원이 아니신가요? <RouterLink :to="{ name: 'signup' }" class="nav-link">회원가입</RouterLink></p>
    </div>
  </template>
  
  <script setup>
  import AuthForm from '@/components/AuthForm.vue'
  </script>
  <style lang="scss" scoped>
  
  </style>