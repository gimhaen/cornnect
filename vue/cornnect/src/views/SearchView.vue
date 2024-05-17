<template>
    <div class="search-container">
        <h3>검색</h3>
        <div class="community-nav">
            <Community />   
        </div>
    </div>
  </template>
  
  <script setup>
    import Community from '@/components/Community.vue'
  </script>
  
  <style scoped>
  .search-container {
    display: flex;
    justify-content: space-between; /* 두 요소 간에 여백 */
    align-items: flex-start; /* 선택 사항: 상단 정렬 */
    height: 100vh; /* 화면의 100% 차지 */
  }
  .community-nav {
    width: 180px;
    padding: 20px;
    border: 1px solid #ccc;
    margin-left: auto /* 우측 끝에 위치시킴 */
  }
  </style>
  
  