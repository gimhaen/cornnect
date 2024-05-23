import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { defineStore } from "pinia";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const user = ref({});
    const router = useRouter();
    const token = ref("");
    const isAuthenticated = ref(false);
    const signUp = function (username, password1, password2) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/auth/signup/",
        data: {
          username,
          // email,
          password1,
          password2,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          console.log(token.value);
          console.log(res.data);
          isAuthenticated.value = true;
          user.value = res.data.user;
          router.push({ name: "login" });
        })
        .catch((err) => {
          console.error(err);
        });
    };

    const logIn = function (username, password) {
      console.log(password);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/auth/login/",
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          isAuthenticated.value = true;
          user.value = res.data.user;
          router.push({ name: "main" });
        })
        .catch((err) => {
          console.error(err);
        });
    };

    const logOut = function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/auth/logout/",
        // headers: {
        //   'Authorization': `Token ${token.value}`
        // }
      })
        .then((res) => {
          token.value = "";
          isAuthenticated.value = false;
          user.value = {};
          router.push({ name: "login" });
        })
        .catch((err) => {
          console.error(err);
        });
    };

    const updateUser = function (updatedUser) {
      axios({
        method: "patch",
        url: "http://127.0.0.1:8000/api/auth/user/",
        headers: {
          Authorization: `Token ${token.value}`,
          "Content-Type": "application/json",
        },
        data: updatedUser,
      })
        .then((res) => {
          user.value = res.data;
          console.log("User updated:", res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    };

    return { signUp, logIn, logOut, updateUser, token, isAuthenticated, user };
  },
  { persist: true }
);
