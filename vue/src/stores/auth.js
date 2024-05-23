import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";
import { useArticleStore } from "@/stores/article.js";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const user = ref({});
    const router = useRouter();
    const articleStore = useArticleStore();
    const token = ref("");
    const isAuthenticated = ref(false);

    const signUp = function (username, password1, password2) {
      return (
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/api/auth/signup/",
          data: { username, password1, password2 },
        })
          .then((res) => {
            // console.log(res);
            // token.value = res.data.key;
            // console.log(token.value);
            // console.log(res.data);
            // isAuthenticated.value = true;
            // user.value = res.data.user;
            logIn(username, password1);
            // router.push({ name: "login" });
          })
          // .then(() => getUserInfo()) // 주석처리
          .catch((err) => console.error(err))
      );
    };

    const getUserInfo = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/auth/user/",
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          user.value = res.data;
        })
        .catch((err) => console.error(err));
    };

    const logIn = function (username, password) {
      console.log(password);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/auth/login/",
        data: { username, password },
      })
        .then((res) => {
          token.value = res.data.key;
          isAuthenticated.value = true;
          router.push({ name: "main" });
        })
        .then(() => {
          //순차 처리 위해 추가
          getUserInfo();
        })
        .catch((err) => console.error(err));
    };

    const logOut = function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/auth/logout/",
        // headers: { 'Authorization': `Token ${token.value}` }
      })
        .then(() => {
          token.value = "";
          isAuthenticated.value = false;
          user.value = {};
          router.push({ name: "login" });
        })
        .catch((err) => console.error(err));
    };

    const updateUser = function (username, profile_pic) {
      const formData = new FormData();
      formData.append("username", username);
      formData.append("profile_pic", profile_pic);
      return axios({
        method: "PUT",
        url: "http://127.0.0.1:8000/api/user/update/",
        headers: {
          Authorization: `Token ${token.value}`,
          "Content-Type": "multipart/form-data",
        },
        data: formData,
      })
        .then((res) => {
          user.value = res.data;
          console.log("User updated:", res.data);
          articleStore.getReviews();
        })
        .catch((err) => console.error(err));
    };

    const showModal = ref(false);

    const profileCloseModal = function () {
      showModal.value = false;
    };

    const profileOpenModal = function () {
      showModal.value = true;
    };

    return {
      signUp,
      logIn,
      logOut,
      updateUser,
      profileOpenModal,
      profileCloseModal,
      token,
      isAuthenticated,
      user,
      showModal,
    };
  },
  { persist: true }
);
