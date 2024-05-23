<template>
  <div
    v-if="articleStore.showModal"
    class="modal-overlay"
    @click.self="closeModal"
  >
    <div class="modal-container">
      <div class="modal-header">
        <div class="modal-subheader">
          <div class="review-header">
            <p>리뷰쓰기</p>
          </div>
          <div class="close-button-container">
            <button class="close-button" @click="closeModal">×</button>
          </div>
        </div>
        <div class="search-input-container">
          <input
            :value="searchTerm"
            @input="onSearchInput"
            @keyup.enter="searchMovies"
            placeholder="영화제목, 배우, 감독 또는 장르를 입력하세요."
            type="text"
            class="search-input"
          />
        </div>
        <div v-if="showResults" class="search-results">
          <ul>
            <li
              v-for="result in searchResults"
              :key="result.id"
              @click="selectSearchResult(result)"
            >
              {{ result.title }}
            </li>
          </ul>
        </div>
      </div>
      <div class="modal-content">
        <textarea
          v-model="content"
          placeholder="재미있게 보셨나요? 작품에 대한 리뷰를 자유롭게 남겨주세요."
          class="input-content"
        ></textarea>
        <input type="file" @change="handleImageChange" />
        <div v-if="previewImage" class="image-preview">
          <img :src="previewImage" alt="Preview" />
        </div>
        <div class="rating-container">
          <span class="rating-label">별점:</span>
          <div class="rating-stars">
            <span
              v-for="(star, index) in 5"
              :key="index"
              @click="setRating(index + 1)"
              :class="{
                filled:
                  index < Math.floor(rating) ||
                  (index === Math.floor(rating) && rating % 1 !== 0),
              }"
              >★</span
            >
          </div>
          <button @click="submitPost" class="submit-button">작성하기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useArticleStore } from "@/stores/article.js";
import { useAuthStore } from "@/stores/auth.js";
import { useMovieStore } from "@/stores/movie.js";

const articleStore = useArticleStore();
const authStore = useAuthStore();

const movieStore = useMovieStore();
const searchTerm = ref("");
const showResults = ref(false);
const tmdb_id = ref(null);

const searchResults = computed(() => {
  return movieStore.movies
    .filter((movie) =>
      movie.title.toLowerCase().includes(searchTerm.value.toLowerCase())
    )
    .slice(0, 5);
});
const router = useRouter();

const onSearchInput = (event) => {
  searchTerm.value = event.target.value;
  if (searchTerm.value.trim() !== "") {
    movieStore.search(searchTerm.value.trim());
    showResults.value = true;
  } else {
    showResults.value = false;
  }
};

const selectSearchResult = (result) => {
  searchTerm.value = result.title;
  showResults.value = false;
  tmdb_id.value = result.tmdb_id;
  // console.log(result.tmdb_id);
  // console.log("이게뭐야이게뭐야");
};

const content = ref("");
const rating = ref(3);
const previewImage = ref(null);
const imageFile = ref(null);
const closeModal = () => {
  tmdb_id.value = null;
  rating.value = 3;
  content.value = "";
  previewImage.value = null;
  imageFile.value = null;
  articleStore.closeModal();
};

const handleImageChange = (event) => {
  const file = event.target.files[0];
  imageFile.value = file;
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      previewImage.value = reader.result;
    };
    reader.readAsDataURL(file);
  }
};

const submitPost = () => {
  articleStore.writeReview(
    tmdb_id.value,
    rating.value,
    content.value,
    imageFile.value
  );
  // console.log(tmdb_id.value);
  closeModal();
};

const setRating = (value) => {
  rating.value = value;
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Pacifico&display=swap");

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
  flex-direction: column;
  align-items: center;
  padding: 0px 10px 10px;
  border-bottom: 1px solid #e6e6e6;
  position: relative;
}

.modal-subheader {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 20px;
}

.review-header {
  width: 100%;
  text-align: center;
}

.review-header p {
  margin: 10px 0px;
}
.close-button-container {
  text-align: right;
  padding-right: 15px;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.search-input-container {
  display: flex;
  width: 100%;
  justify-content: center;
}

.search-input {
  width: calc(100% - 40px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  outline: none;
  font-size: 16px;
}

.search-button {
  width: 40px;
  background-color: #007bff;
  border: none;
  color: white;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}

.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background: white;
  border: 1px solid #ccc;
  border-radius: 0 0 4px 4px;
  z-index: 1001;
}

.search-results ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.search-results li {
  padding: 10px;
  cursor: pointer;
}

.search-results li:hover {
  background-color: #f0f0f0;
}

.modal-content {
  padding: 15px 20px 5px;
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
  text-align: bottom;
}

.rating-stars {
  color: #fff88f;
}

.rating-stars span {
  font-size: 24px;
  cursor: pointer;
}

.rating-stars span.filled {
  color: #ffbb00;
}

.image-preview {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

.image-preview img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
