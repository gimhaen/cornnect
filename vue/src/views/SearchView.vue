<!-- <template>
    <div class="search-container">
        <h3>검색</h3>
      <div class="talk-list-nav">
          <TalkList />   
      </div>
  </div>
</template> -->
<template>
  <div class="search-container">
    <div class="search-page">
      <div class="search-card">
        <input type="text" v-model="searchQuery" @input="searchMovies" placeholder="Search">
        <div v-if="isLoading">로딩 중...</div>
        <div v-else-if="errorMessage">에러: {{ errorMessage }}</div>
        <div v-else>
          <div v-for="movie in movies" :key="movie.id">
            <h2>{{ movie.title }}</h2>
            <p>개봉 연도: {{ movie.releaseYear }}</p>
            <p>평점: {{ movie.rating }}</p>
          </div>
        </div>
      </div>
      <BoxOffice class="box-office" />
    </div>

    <div class="talk-list-nav">
      <TalkList />   
    </div>
  </div>
</template>
  
<script setup>
  import { ref } from 'vue';
  import TalkList from '@/components/TalkList.vue'
  import BoxOffice from '@/components/BoxOffice.vue'

  const searchQuery = ref('');
  const movies = ref([]);
  const isLoading = ref(false);
  const errorMessage = ref('');

  const searchMovies = async () => {
    if (!searchQuery.value) {
      return;
    }
    isLoading.value = true;
    try {
      // 여기서 실제 API 엔드포인트를 사용하세요
      const response = await fetch(`https://api.example.com/movies?search=${searchQuery.value}`);
      const data = await response.json();
      movies.value = data;
      errorMessage.value = '';
    } catch (error) {
      errorMessage.value = '영화를 불러오는 중에 오류가 발생했습니다.';
    } finally {
      isLoading.value = false;
    }
  };
</script>

<!-- <style scoped>
.search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style> -->

  
<!-- <script setup>
  import TalkList from '@/components/TalkList.vue'
</script> -->

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

input[type="text"] {
  width: 80%;
  min-width: 400px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px; /* 동그랗게 만들기 */
  font-size: 16px; /* 텍스트 크기 */
  outline: none; /* 포커스시 테두리 제거 */
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
