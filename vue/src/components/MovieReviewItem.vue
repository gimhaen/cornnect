<template>
  <div>
    <div class="post">
      <div class="post-container">
        <img
          v-if="review.user.profile_pic"
          :src="'http://127.0.0.1:8000' + review.user.profile_pic"
          alt="user img"
          class="user-img"
        />
        <img
          v-if="!review.user.profile_pic"
          src="@/assets/뛰는 치이카와.png"
          alt="user img"
          class="user-img"
        />
        <div>
          <div class="post-info">
            <div class="user-info">
              <h4>
                {{ review.user.username }}
              </h4>
              <p class="post-time">{{ formatDate(review.created_at) }}</p>
            </div>
            <div class="rating-movie">
              <div class="rating-stars">
                <span v-for="n in review.rating" :key="n">★</span>
              </div>
            </div>
          </div>
          <p class="post-content">{{ review.content }}</p>

          <img
            v-if="review.review_image"
            :src="'http://127.0.0.1:8000' + review.review_image"
            alt="post img"
            class="post-img"
          />
          <div class="post-actions">
            <button class="icon-button">
              <font-awesome-icon icon="thumbs-up" />
            </button>
            <span class="post-icon-content">좋아요</span>
            <button class="icon-button">
              <font-awesome-icon icon="comment" />
            </button>
            <span class="post-icon-content">댓글</span>
          </div>
        </div>
      </div>
      <hr />
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  review: Object,
});

// const authStore = useAuthStore();
// const user = computed(()=> {
//   return authStore.user
// })

const formatDate = (timeString) => {
  const date = new Date(timeString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const hour = String(date.getHours()).padStart(2, "0");
  const minute = String(date.getMinutes()).padStart(2, "0");
  return `${year}.${month}.${day}. ${hour}:${minute}`;
};
</script>

<style scoped>
.post {
  /* background: white;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px; */
}

.post-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.user-info {
  display: flex;
  flex-direction: column;
  margin-right: 20px;
}

h4 {
  margin: 0;
  padding: 12px 0px 5px;
}

.post-time {
  margin-top: 0;
  font-size: 13px;
  color: #888;
}

.rating-movie {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-left: auto;
}

.rating-movie-title {
  margin-left: auto;
  width: 100%;
  padding: 10px;
}
.rating-movie-title p {
  font-size: 13px;
  color: #888;
  margin: 0;
  text-align: right;
}
.rating-stars {
  margin-left: auto;
  font-size: 20px;
  color: #ffbb00;
  text-align: center;
}

.post-content {
  margin-top: 0;
}

.user-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
  margin-bottom: auto;
  margin-top: 10px;
}

.post-img {
  width: 500px;
  max-height: 500px;
  object-fit: contain;
}

.post-icon-img {
  width: 40px;
  height: 40px;
}

.post-icon-content {
  margin-right: 40px;
  font-size: 14px;
  color: #555;
}

.post-content {
  font-size: 1rem;
  margin-bottom: 15px;
  width: 500px;
}

.post-actions {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.post-info {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.icon-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 22px;
  color: #999;
} 
</style>
