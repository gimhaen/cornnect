import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PiniaPluginPersistedState from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(PiniaPluginPersistedState)
app.use(pinia)
app.use(router)

app.mount('#app')

import axios from 'axios'

// Vue.config.productionTip = false

// Vue.prototype.$http = axios

// new Vue({
//   render: h => h(App),
// }).$mount('#app')