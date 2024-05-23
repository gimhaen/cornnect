import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
export const useMovieStore = defineStore("movie", () => {
  const movies = ref([]);
  const movie = ref(null);
  const searchQuery = ref("");
  const authStore = useAuthStore();

  const search = function (searchText) {
    return axios({
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

  const movie_detail = function (tmdb_id) {
    return axios({
      method: "get",
      url: `http://127.0.0.1:8000/movies/${tmdb_id}/`,
      headers: {
        Authorization: `Token ${authStore.token}`,
      },
    })
      .then((response) => {
        movie.value = response.data;
        // console.log(response.data);
      })
      .catch((error) => {
        console.error("Error searching movies:", error);
      });
  };
  return { movies, movie, search, movie_detail };
});
