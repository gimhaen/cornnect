import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
export const useMovieStore = defineStore("movie", () => {
  const movies = ref([]);
  const searchQuery = ref("");
  const authStore = useAuthStore();

  const search = function (searchText) {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/movies/search/",
      params: {
        searchTerm: searchText,
      },
      headers: {
        Authorization: `Token ${authStore.token}`,
      },
    })
      .then((response) => {
        movies.value = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.error("Error searching movies:", error);
      });
  };

  return { movies, search };
});
