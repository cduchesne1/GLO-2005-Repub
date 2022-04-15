import Vue from 'vue';
import App from './App.vue';
import router from "./navigation/router";
import "./index.css";

const store = Vue.observable({
  user: {
    name: "Devin Fenech",
    username: "dfenech0",
    email: "dfenech0@reverbnation.com",
    id: 1,
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
