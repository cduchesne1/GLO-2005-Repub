import Vue from "vue";
import Router from "vue-router";
import LoggedHomePage from "@/pages/LoggedHomePage";
import LoginPage from "@/pages/LoginPage";
import SignUp from "@/pages/SignUp";
import ProfilePage from "@/pages/ProfilePage";
import RepositoryPage from "@/pages/RepositoryPage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: LoggedHomePage,
    },
    {
      path: "/login",
      name: "Login",
      component: LoginPage,
    },
    {
      path: "/signup",
      name: "Signup",
      component: SignUp,
    },
    {
        path: "/profile",
        name: "Profile",
        component: ProfilePage,
    },
    {
      path: "/repository",
      name: "Repository",
      component: RepositoryPage,
    }
  ],
});