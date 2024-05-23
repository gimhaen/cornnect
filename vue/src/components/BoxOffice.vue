<template>
  <div id="app">
    <h1>박스오피스 순위</h1>
    <div v-if="movies" class="boxoffice-container">
        <div v-for="movie in movies.slice(0, 5)" :key="movie.movieCd" class="boxoffice-card">
          <div v-if="movie.rank == 1" style="color: red;">
            <p class="boxoffice-sales-share">예매율 {{ movie.salesShare }}%</p>
          </div>
          <div v-else-if="movie.rank == 2" style="color: orangered;">
            <p class="boxoffice-sales-share">예매율 {{ movie.salesShare }}%</p>
          </div>
          <div v-else-if="movie.rank == 3" style="color: orange;">
            <p class="boxoffice-sales-share">예매율 {{ movie.salesShare }}%</p>
          </div>
          <div v-else style="color: rgb(255, 218, 7);">
            <p class="boxoffice-sales-share">예매율 {{ movie.salesShare }}%</p>
          </div>
          <p class="boxoffice-movie-name">{{ movie.rank }}. {{ movie.movieNm }}</p>
          <p class="boxoffice-audi-acc">누적관객수 {{ movie.audiAcc }}명</p>
        </div>
    </div>
    <div v-else>
      Loading...
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const movies = ref(null);

const getBoxOfficeData = () => {
  const today = new Date(); // 현재 날짜
  const yesterday = new Date(today);
  yesterday.setDate(today.getDate() - 1); // 어제 날짜

  const year = yesterday.getFullYear(); // 연도
  const month = String(yesterday.getMonth() + 1).padStart(2, '0'); // 월
  const day = String(yesterday.getDate()).padStart(2, '0'); // 일

  const formattedDate = `${year}${month}${day}`; // YYYYMMDD 형식으로 변환

  const url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json";
  const params = {
    'key': '2083a37ad3c34c2ad3a8f96bbbaeba31',
    'targetDt': formattedDate  // 어제 날짜로 설정합니다.
  };

  axios.get(url, { params })
    .then(response => {
      console.log(response.data.boxOfficeResult.dailyBoxOfficeList);  // 서버로부터 받은 데이터 출력
      movies.value = response.data.boxOfficeResult.dailyBoxOfficeList.map(movie => ({
        ...movie,
        audiAcc: movie.audiAcc.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") // 3자리씩 끊어 따옴표 추가
      }));
      console.log(movies.value);
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
};

getBoxOfficeData();
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}

.boxoffice-container {
  text-align: start;
}

.boxoffice-card {
  margin-top: 25px;
}

.boxoffice-sales-share {
  font-size: 13px;
  margin: 0;
  padding: 0;
}

.boxoffice-movie-name {
  font-size: 15px;
  font-weight: bold;
  margin: 0;
  padding: 0;
}

.boxoffice-audi-acc {
  font-size: 12px;
  color: #777;
  margin: 0;
  padding: 0;
}
</style>