<template>
  <div id="app">
    <h1>일간 박스오피스</h1>
    <div v-if="movies">
        <div v-for="movie in movies" :key="movie.movieCd">
          <p>예매율 {{ movie.salesShare }}%</p>
          <p>{{ movie.rank }}. {{ movie.movieNm }}</p>
          <p>누적관객수 {{ movie.audiAcc }}명</p>
        </div>
    </div>
    <div v-else>
      Loading...
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
// import { onMounted } from 'vue'; 
const movies = ref('adf')

const getBoxOfficeData = () => {
  const url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json";
  const params = {
    'key': '2083a37ad3c34c2ad3a8f96bbbaeba31',
    'targetDt': '20190102'  // 기본값으로 오늘 날짜를 설정합니다.
  };

  axios.get(url, { params })
    .then(response => {
      console.log(response.data.boxOfficeResult.dailyBoxOfficeList);  // 서버로부터 받은 데이터 출력
      movies.value = response.data.boxOfficeResult.dailyBoxOfficeList
      console.log(movies.value)
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
};

getBoxOfficeData()

</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}

</style>