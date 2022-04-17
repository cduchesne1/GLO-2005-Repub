import Vue from 'vue';
import App from './App.vue';
import router from "./navigation/router";
import Clipboard from 'v-clipboard'
import "./index.css";

Vue.use(Clipboard)

const store = Vue.observable({
  user: {
    name: "Andrei Bon",
    username: "abon16",
    email: "abon16@harvard.edu",
    id: 43,
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
  setId(id) {
    store.user.id = id;
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
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
