<template>
  <div v-if="articleStore.showModal" class="modal-overlay" @click.self="closeModal">
    <div class="modal-container">
      <!-- <div class="modal-header">
      </div> -->
      <button class="close-button" @click="closeModal">×</button>
      <div class="modal-content">
        <textarea
          v-model="content"
          placeholder="리뷰를 작성하세요..."
          class="input-content"
        ></textarea>
        <input type="file" @change="handleImageChange"> <!-- 이미지 파일을 선택하는 input 추가 -->
        <div v-if="previewImage" class="image-preview"> <!-- 미리보기를 표시할 요소 -->
          <img :src="previewImage" alt="Preview">
        </div>
        <div class="rating-container">
          <span class="rating-label">별점:</span>
          <div class="rating-stars">
            <span
              v-for="(star, index) in 5"
              :key="index"
              @click="setRating(index + 1)"
              :class="{ 'filled': index < Math.floor(rating) || (index === Math.floor(rating) && rating % 1 !== 0) }"
            >★</span>
          </div>
          <button @click="submitPost" class="submit-button">Post</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article.js';
import { useAuthStore } from '@/stores/auth.js';

const articleStore = useArticleStore();
const authStore = useAuthStore();

const content = ref('');
const rating = ref(5);
const previewImage = ref(null); // 이미지 미리보기를 위한 상태 추가
const imageFile = ref(null)
const closeModal = () => {
  rating.value = 5
  content.value = ""
  previewImage.value = null
  imageFile.value = null
  articleStore.closeModal();
};

const handleImageChange = (event) => {
  const file = event.target.files[0];
  imageFile.value = file
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      previewImage.value = reader.result; // 선택된 이미지를 미리보기에 표시
    };
    reader.readAsDataURL(file);
  }
};

const submitPost = () => {
 
  console.log(rating.value, content.value, imageFile.value)
  const movie_id = 1
  articleStore.writeReview(movie_id, rating.value, content.value, imageFile.value)
 
  closeModal()



};

const setRating = (value) => {
  rating.value = value;
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-container {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  width: 500px;
  max-width: 100%;
}

.modal-header {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
  border-bottom: 1px solid #e6e6e6;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.modal-content {
  padding: 20px;
}

.input-title,
.input-content {
  width: 95%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.input-content {
  min-height: 100px;
  resize: vertical;
}

.submit-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-left: auto;
}

.submit-button:hover {
  background-color: #0056b3;
}

.rating-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.rating-label {
  margin-right: 10px;
}

.rating-stars {
  color: #fff88f; /* Yellow color for stars */
}

.rating-stars span {
  font-size: 24px;
  cursor: pointer;
}

.rating-stars span.filled {
  color: #ffbb00; /* Filled star color */
}

/* .image-preview {
  justify-content: center;
} */
</style>
