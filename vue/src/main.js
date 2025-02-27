import { createApp } from "vue";
import { createPinia } from "pinia";
import PiniaPluginPersistedState from "pinia-plugin-persistedstate";

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { faHouse } from "@fortawesome/free-solid-svg-icons";
import { faFilm } from "@fortawesome/free-solid-svg-icons";
import { faPencil } from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import { faComment } from "@fortawesome/free-solid-svg-icons";

import App from "./App.vue";
import router from "./router";

// 사용할 아이콘을 라이브러리에 추가
library.add(faSearch);
library.add(faHouse);
library.add(faFilm);
library.add(faPencil);
library.add(faUser);
library.add(faThumbsUp);
library.add(faComment);

const app = createApp(App);
const pinia = createPinia();

// 전역으로 등록
app.component("font-awesome-icon", FontAwesomeIcon);

pinia.use(PiniaPluginPersistedState);
app.use(pinia);
app.use(router);

app.mount("#app");

import axios from "axios";

// Vue.config.productionTip = false

// Vue.prototype.$http = axios

// new Vue({
//   render: h => h(App),
// }).$mount('#app')

// import axios from 'axios'

// axios.defaults.xsrfHeaderName = 'X-CSRFToken'
// axios.defaults.xsrfCookieName = 'csrftoken'
