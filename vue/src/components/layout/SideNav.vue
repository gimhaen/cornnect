<template>
  <nav class="nav-ver">
    <div class="container-nav">
      <RouterLink :to="{ name: 'main' }" class="nav-link">홈</RouterLink>
      <RouterLink :to="{ name: 'search' }" class="nav-link">검색</RouterLink>
      <RouterLink to="/" class="nav-link">위시리스트</RouterLink>
    </div>

    <button class="write-button" @click="openModal">작성하기</button>
    <div v-if="!isAuthenticated">
      <RouterLink :to="{ name: 'login' }" class="nav-link"
        >로그인/회원가입</RouterLink
      >
    </div>
    <div v-else>
      <a href="#" @click="logOut" class="nav-link">Logout</a>
      <div class="container-nav user-nav">
        <RouterLink :to="{ name: 'user' }" class="nav-link">프로필</RouterLink>
      </div>
    </div>
    <div>
      <!-- 별점 관련 코드 -->
      <!-- <WritePage v-if="showModal" @close="closeModal" :movie="movie"/> -->
      <!-- 별점 관련 코드 -->
    </div>
  </nav>
</template>

<script setup>
// import { RouterView, RouterLink } from 'vue-router'
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import WritePage from "@/components/WritePage.vue";
import { useArticleStore } from "@/stores/article.js";
import { useAuthStore } from "@/stores/auth";
const articleStore = useArticleStore();

// 모달 열고 닫는 showModal
const showModal = ref(false);

// 클릭시 모달 열리는 함수
const openModal = () => {
  articleStore.showModal = true;
};

// 클릭시 모달 닫히는 함수

// 로그아웃 함수
const authStore = useAuthStore();
const router = useRouter();

const isAuthenticated = computed(() => authStore.isAuthenticated);

const logOut = () => {
  authStore.logOut();
  router.push({ name: "login" });
};
</script>

<style scoped>
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
  margin-bottom: 20px;
}

.write-button {
  width: auto; /* 너비 자동 조정 */
  /* margin-top: auto; 버튼을 아래로 이동 */
  /* align-self: flex-start; 버튼이 왼쪽에 위치하도록 설정 */
}

.user-nav {
  margin-top: auto;
}
</style>
