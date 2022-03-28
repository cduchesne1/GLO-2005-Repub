import Vue from "vue";
import Router from "vue-router";
import HomePage from "@/pages/HomePage";
import ProfilePage from "@/pages/ProfilePage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomePage,
    },
    {
        path: "/profile",
        name: "Profile",
        component: ProfilePage,
    },
  ],
});