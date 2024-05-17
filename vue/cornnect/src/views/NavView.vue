<template>
<<<<<<< HEAD:vue/cornnect/src/views/NavView.vue
    <nav class="nav-ver">
        <div class="container-nav">
        <RouterLink :to="{ name: 'MainView' }" class="nav-link">홈</RouterLink>
        <RouterLink :to="{ name: 'SearchView' }" class="nav-link">검색</RouterLink>
        <RouterLink :to="{ name: 'MovieView' }" class="nav-link">영화</RouterLink>
        </div>

        <button class="write-button">작성하기</button>
        <div class="container-nav profile-nav">
        <RouterLink :to="{ name: 'ProfileView' }" class="nav-link">프로필</RouterLink>
        </div>
    </nav>
=======
        <nav class="nav-ver">
          <div class="container-nav">
            <RouterLink :to="{ name: 'main' }" class="nav-link">홈</RouterLink>
            <RouterLink :to="{ name: 'movie' }" class="nav-link">검색</RouterLink>
            <RouterLink :to="{ name: 'movie' }" class="nav-link">영화</RouterLink>
          </div>
  
          <button class="write-button">작성하기</button>
          <div class="container-nav profile-nav">
            <RouterLink :to="{ name: 'profile' }" class="nav-link">프로필</RouterLink>
          </div>
        </nav>

>>>>>>> dbb8c02f35cfa1545ac65860bf9bd142c40a6461:vue/cornnect/src/components/Nav.vue
  </template>
  
  <script setup>
  import { RouterView, RouterLink } from 'vue-router'
  </script>
  
  <style scoped>
  .nav-ver {
    position: fixed; /* 고정 */
    width: 80px;
    height: 80%;
    display: flex;
    flex-direction: column; /* 세로로 배열 */
    align-items: center;
    text-align: center;


    padding: 20px;
    border: 1px solid #ccc;
  }
  
  .container-nav {
    display: flex;
    flex-direction: column;
  }
  
  .nav-link {
    margin-bottom: 20px;
  }
  
  .write-button {
    width: auto; /* 너비 자동 조정 */
    /* margin-top: auto; 버튼을 아래로 이동 */
    /* align-self: flex-start; 버튼이 왼쪽에 위치하도록 설정 */
  }

  .profile-nav {
    margin-top: auto;
  }
  </style>
  