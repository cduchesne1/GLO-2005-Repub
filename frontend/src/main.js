import Vue from 'vue';
import App from './App.vue';
import VueCookie from "vue-cookies";
import router from "./navigation/router";
import Clipboard from 'v-clipboard'
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import "./index.css";

Vue.component("v-select", vSelect);
Vue.use(Clipboard)

const store = Vue.observable({
  user: {
    name: "",
    username: "",
    email: "",
  },
  isConnected: false,
});

const actions = {
  setName(name) {
    store.user.name = name;
  },
  setUsername(username) {
    store.user.username = username;
  },
  setEmail(email) {
    store.user.email = email;
  },
  connect() {
    store.isConnected = true;
  },
  disconnect() {
    store.isConnected = false;
  }
};

Vue.prototype.$store = store;
Vue.prototype.$actions = actions;
Vue.config.productionTip = false;

Vue.use(VueCookie);

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
