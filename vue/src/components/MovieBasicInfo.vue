<template>
  <div class="movie-detail">
    <div>
      <h3>설명</h3>
      <p>{{ movie.description }}</p>
    </div>
    <div>
      <h3>장르</h3>
      <ul>
        <li v-for="(genre, index) in movie.genres" :key="index">
          {{ genre.name }}
        </li>
      </ul>
    </div>
    <div v-if="movie.director">
      <h3>감독</h3>
      <img
        :src="movie.director.profile_image"
        :alt="movie.director.name"
        class="director-image"
      />
      <p>{{ movie.director.name }}</p>
    </div>
    <div class="actors">
      <h3>배우들</h3>
      <div v-if="movie.actors" class="actor-list">
        <div v-for="(actor, index) in movie.actors" :key="index" class="actor">
          <img
            :src="actor.profile_image"
            :alt="actor.name"
            class="actor-image"
          />
          <p>{{ actor.name }}</p>
        </div>
      </div>
    </div>

    <div>
      <h3>출시 연도</h3>
      <p>{{ movie.release_year }}</p>
    </div>
    <div>
      <h3>러닝 타임</h3>
      <p>{{ movie.running_time }} 분</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useMovieStore } from "@/stores/movie.js";

const movieStore = useMovieStore();
const route = useRoute();
const movie = ref({});

onMounted(() => {
  movieStore
    .movie_detail(route.params.tmdb_id)
    .then(() => {
      movie.value = movieStore.movie;
    })
    .catch((error) => {
      console.error("Error fetching movie detail:", error);
    });
});
</script>
<style scoped>
.director-image {
  width: 150px; /* 이미지의 너비를 조정하여 크기를 줄입니다 */
  height: auto;
  border-radius: 5px;
  margin-bottom: 10px;
}

.actor-list {
  display: flex;
  flex-wrap: nowrap; /* 줄 바꿈 방지 */
  overflow-x: auto; /* 가로 스크롤바 추가 */
}

.actor {
  display: inline-flex; /* 배우 요소를 인라인 플렉스로 설정하여 가로로 나란히 배치 */
  flex-direction: column; /* 이미지와 이름을 세로로 나란히 배치 */
  align-items: center; /* 이미지와 이름을 가운데 정렬 */
  margin-right: 20px; /* 각 배우 요소 사이의 오른쪽 여백 추가 */
}

.actor:last-child {
  margin-right: 0; /* 마지막 배우 요소의 오른쪽 여백 제거 */
}

.actor-image {
  width: 150px; /* 배우 이미지의 너비를 조정하여 크기를 줄입니다 */
  height: auto;
  border-radius: 5px;
  margin-bottom: 10px;
}

.actor p {
  font-size: 14px;
  font-weight: bold;
  text-align: center;
  white-space: nowrap; /* 긴 배우 이름을 줄여주기 위해 줄 바꿈 방지 */
  overflow: hidden; /* 긴 배우 이름을 숨김 */
  text-overflow: ellipsis; /* 긴 배우 이름을 생략 부호로 표시 */
}
</style>
