<template>
  <nav class="nav-ver">
    <div class="container-nav">
      <RouterLink :to="{ name: 'main' }" class="nav-link logo-link">
        <div class="nav-logo pacifico-regular">cornnect</div>
      </RouterLink>
      <RouterLink :to="{ name: 'main' }" class="nav-link">
        <!-- <button class="search-button" @click="searchMovies"> -->
        <button class="icon-button">
          <font-awesome-icon icon="house" />
        </button>
      </RouterLink>
      <RouterLink :to="{ name: 'search' }" class="nav-link">
        <button class="icon-button">
          <font-awesome-icon icon="search" />
        </button>
      </RouterLink>
      <RouterLink to="/" class="nav-link">
        <button class="icon-button">
          <font-awesome-icon icon="film" />
        </button>
      </RouterLink>
    </div>

    <button class="write-button icon-button" @click="openModal">
      <font-awesome-icon icon="pencil" />
    </button>

    <div class="user-nav">
      <div v-if="!isAuthenticated">
        <RouterLink :to="{ name: 'login' }" class="nav-link">Login</RouterLink>
      </div>
      <div v-else>
        <div class="profile-nav">
          <a href="#" @click.prevent="profileDropdown" class="nav-link">
            <div v-if="user.profile_pic">
              <img
                :src="'http://127.0.0.1:8000' + user.profile_pic"
                alt="user img"
                class="user-img"
              />
              <!-- <p class="user-username">{{ user.username }}</p> -->
            </div>
            <button v-if="!user.profile_pic" class="icon-button">
              <font-awesome-icon icon="user" />
            </button>
          </a>
          <div v-if="profileShowDropdown" class="profile-menu">
            <!-- <RouterLink :to="{ name: 'user' }" @click.prevent="profileDropdown" class="profile-dropdown-item">상세 프로필</RouterLink> -->
            <a
              href="#"
              class="profile-button profile-dropdown-item"
              @click="profileOpenModal"
              >프로필 수정</a
            >
            <a
              href="#"
              @click="logOut"
              @click.prevent="profileDropdown"
              class="profile-dropdown-item"
              >Logout</a
            >
          </div>
        </div>
        <!-- <a href="#" @click="logOut" class="nav-link">Logout</a>
        <div class="container-nav user-nav">
          <RouterLink :to="{ name: 'user' }" class="nav-link">프로필</RouterLink>
        </div> -->
      </div>
    </div>
    <div>
      <!-- 별점 관련 코드 -->
      <!-- <MainWritePage v-if="showModal" @close="closeModal" :movie="movie"/> -->
      <!-- 별점 관련 코드 -->
    </div>
  </nav>
</template>

<script setup>
// import { RouterView, RouterLink } from 'vue-router'
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
// import MainWritePage from "@/components/MainWritePage.vue";
import { useArticleStore } from "@/stores/article.js";
import { useAuthStore } from "@/stores/auth";

const articleStore = useArticleStore();
const authStore = useAuthStore();
const router = useRouter();

// 모달 열고 닫는 showModal
// const showModal = ref(false);
const profileShowDropdown = ref(false);

const isAuthenticated = computed(() => authStore.isAuthenticated);
const user = computed(() => authStore.user);

// 클릭시 모달 열리는 함수
const openModal = () => {
  articleStore.showModal = true;
};

const profileOpenModal = () => {
  authStore.showModal = true;
};

const profileDropdown = () => {
  profileShowDropdown.value = !profileShowDropdown.value;
};

const logOut = () => {
  authStore.logOut();
  router.push({ name: "login" });
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Pacifico&display=swap");

.pacifico-regular {
  font-family: "Pacifico", cursive;
  font-weight: 400;
  font-style: normal;
}

.nav-logo {
  font-size: 25px; /* 글꼴 크기 조정 */
  color: #000; /* 글꼴 색상 조정 */
}

.nav-ver {
  position: fixed; /* 고정 위치 설정 */
  width: 80px; /* 세로 너비의 20%로 설정 */
  height: 80%; /* 화면 높이의 80%로 설정 */
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;

  padding: 20px; /* 선택 사항: 게시글 영역에 여백 추가 */
  border: 1px solid #ccc; /* 선택 사항: 게시글 영역에 테두리 추가 */
}

.container-nav {
  display: flex;
  flex-direction: column;
}

.nav-link {
  margin-bottom: 30px;
  text-decoration: none; /* 밑줄 제거 */
}

.nav-link.logo-link {
  text-decoration: none; /* 로고 링크 밑줄 제거 */
}

.nav-link.logo-link:hover .nav-logo {
  text-decoration: none; /* 로고 링크 호버 시에도 밑줄 제거 */
}

.write-button {
  width: auto; /* 너비 자동 조정 */
  /* margin-top: auto; 버튼을 아래로 이동 */
  /* align-self: flex-start; 버튼이 왼쪽에 위치하도록 설정 */
}

.user-nav {
  margin-top: auto;
}

.profile-nav {
  margin-top: auto;
  position: relative;
}

.profile-menu {
  position: absolute;
  bottom: 0%;
  left: 110%;
  display: flex;
  flex-direction: column;
  background-color: white;
  border: 1px solid #ccc;
  width: 120px;
}

.profile-dropdown-item {
  padding: 10px;
  text-align: center;
  cursor: pointer;
}

.profile-dropdown-item:hover {
  background-color: #f0f0f0;
}

.icon-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 27px;
  color: #999;
}

.user-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-right: 10px;
  margin-bottom: auto;
  margin-top: 10px;
}
</style>
