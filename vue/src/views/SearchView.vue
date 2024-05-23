<!-- SearchView.vue -->
<template>
  <div class="search-container">
    <div class="search-page">
      <div class="search-card">
        <div class="search-input-container">
          <input
            v-model="searchTerm"
            @input="onSearchInput"
            @keyup.enter="searchMovies"
            placeholder="영화제목, 배우, 감독 또는 장르를 입력하세요."
            type="text"
          />
          <button class="search-button" @click="searchMovies">
            <font-awesome-icon icon="search" />
          </button>
        </div>

        <div class="movies-grid" v-if="movies.length > 0">
          <div
            v-for="movie in movies"
            :key="movie.id"
            class="movie-card"
            @click="goToMovieDetail($event, movie.tmdb_id)"
          >
            <img
              :src="movie.poster_image"
              :alt="movie.title"
              class="movie-poster"
            />
            <h2>{{ movie.title }}</h2>
            <p>{{ movie.tmdb_id }}</p>
          </div>
        </div>
        <div v-else v-show="showResults">
          <p>검색 결과가 없습니다.</p>
        </div>
      </div>
      <BoxOffice v-show="!showResults" class="box-office" />
    </div>

    <div class="talk-list-nav">
      <TalkList />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import TalkList from "@/components/TalkList.vue";
import BoxOffice from "@/components/BoxOffice.vue";
import { useMovieStore } from "@/stores/movie.js";

// 검색 결과 받아오기
const movieStore = useMovieStore();
const searchTerm = ref("");
const showResults = ref(false);
const router = useRouter();

const onSearchInput = (event) => {
  searchTerm.value = event.target.value;
};

const searchMovies = () => {
  if (searchTerm.value.trim() !== "") {
    movieStore.search(searchTerm.value);
    showResults.value = true;
  }
};

const movies = computed(() => movieStore.movies);

// 영화 상세 페이지로 가기
const goToMovieDetail = (event, tmdb_id) => {
  router.push({ path: `/movie/${tmdb_id}` });
};

// 검색 페이지(SearchView.vue)에서 다른 페이지로 이동할 때마다 movies 초기화
router.beforeEach((to, from, next) => {
  if (from.name === "search" && to.name !== "search") {
    movieStore.movies = [];
  }
  next();
});
</script>

<style scoped>
.search-container {
  display: flex;
  justify-content: center; /* 검색을 가운데 정렬 */
  align-items: flex-start; /* 세로 중앙 정렬 */
  height: 100vh;
}

.search-page {
  flex-grow: 1; /* 입력란과 내용이 같이 컨테이너를 차지할 수 있도록 함 */
  display: flex;
  flex-direction: column; /* 수직으로 정렬 */
}

.search-card {
  display: flex;
  flex-direction: column;
  align-items: center; /* 가로 중앙 정렬 */
  justify-content: center;
}

.search-input-container {
  display: flex;
  align-items: center;
  width: 80%;
  min-width: 400px;
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 5px 10px;
}

.search-input-container input {
  flex-grow: 1;
  border: none;
  outline: none;
  font-size: 16px;
}

.search-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 18px;
  color: #666;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(
    auto-fill,
    minmax(200px, 1fr)
  ); /* 반응형 그리드 설정 */
  gap: 20px;
  width: 100%;
  padding: 20px;
}

.movie-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  text-align: center;
}

.movie-poster {
  width: 100%;
  height: 300px;
  display: block;
}

.movie-card h2 {
  font-size: 18px;
  margin: 10px 0;
  padding: 0 10px;
}

.talk-list-nav {
  width: 180px;
  padding: 20px;
  border: 1px solid #ccc;
  margin-left: 20px; /* 좌우 여백 추가 */
}

.box-office {
  margin-left: 40px; /* 박스오피스를 왼쪽으로 붙이기 위한 여백 추가 */
}
</style>
