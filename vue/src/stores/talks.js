import axios from "axios";
import { defineStore } from "pinia";
import { useArticleStore } from "./article.js";
import { useAuthStore } from "./auth.js";
import { ref } from "vue";

export const useTalkStore = defineStore(
  "talk",
  () => {
    const token = useAuthStore().token;
    const postStore = useArticleStore();
    const talks = ref([])
    const getTalks = async (tmdb_id) => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/movies/${tmdb_id}/talks/`,
          {
            headers: {
                Authorization: `Token ${token}`,
            },
            }
        );
        talks.value = response.data;
        console.log(talks.value)
      } catch (error) {
        console.error(error);
      }
    //   console.log(tmdb_id)
    };

    const talkCreate = async (tmdb_id, content) => {
        
      try {
        const response = await axios.post(
          `http://127.0.0.1:8000/movies/${tmdb_id}/talk/create/`,
          { content },
          {
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );
      
      } catch (error) {
        console.error(error);
      }

    //   console.log(tmdb_id)
    };

    const talkDelete = async (tmdb_id, talk_id) => {
      try {
        await axios.delete(`http://127.0.0.1:8000/movies/${tmdb_id}/talk/${talk_id}/`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        postStore.detailPost.talks = postStore.detailPost.talks.filter(
          (talk) => talk.id !== talkPk
        );
      } catch (error) {
        console.error(error);
      }
    };

    return { talks, getTalks, talkCreate, talkDelete };
  },
  { persist: true }
);
