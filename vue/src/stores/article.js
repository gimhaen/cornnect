import axios from "axios";
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import { useAuthStore } from "@/stores/auth.js";

export const useArticleStore = defineStore(
  "article",
  () => {
    const authStore = useAuthStore();

    const showModal = ref(false);
    const router = useRouter();
    const articles = ref([]);
    const reviews = ref([]);

    const closeModal = function () {
      showModal.value = false;
    };

    const openModal = function () {
      showModal.value = true;
    };

    const addArticle = function (article) {
      articles.value.push(article);
    };

    const getReviews = function () {
      console.log(authStore.token);
      return axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/reviews/`,
        headers: {
          Authorization: `Token ${authStore.token}`,
          // 'Content-Type': 'application/json'
        },
      })
        .then((res) => {
          reviews.value = res.data;
          return res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    };

    const writeReview = function (movie_id, rating, content, imageFile) {
      console.log(`Token ${authStore.token}`);
      console.log(rating);
      console.log(content);
      const formData = new FormData();
      formData.append("rating", rating);
      formData.append("content", content);
      formData.append("review_image", imageFile);
      console.log("write");
      console.log(formData);
      return axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/${movie_id}/review/`,
        headers: {
          Authorization: `Token ${authStore.token}`,
          "Content-Type": "multipart/form-data", // 파일 업로드를 위해 Content-Type 설정
        },
        data: formData,
      })
        .then((res) => {
          getReviews();
          console.log(res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    };

    return {
      openModal,
      closeModal,
      addArticle,
      writeReview,
      getReviews,
      showModal,
      articles,
      reviews,
    };
  },
  { persist: false }
);
