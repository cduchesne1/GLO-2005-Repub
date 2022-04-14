import Vue from "vue";
import Router from "vue-router";
import LoggedHomePage from "@/pages/LoggedHomePage";
import LoginPage from "@/pages/LoginPage";
import SignUp from "@/pages/SignUp";
import ProfilePage from "@/pages/ProfilePage";
import RepositoryPage from "@/pages/RepositoryPage";
import UserTasksPage from "@/pages/UserTasksPage";
import SettingsPage from "@/pages/SettingsPage";

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
    },
    {
      path: "/tasks",
      name: "Tasks",
      component: UserTasksPage,
    },
    {
      path:"/settings",
      name: "Settings",
      component:SettingsPage,
    },
    {
      path:"/settings/profil",
      name: "SettingsProfil",
      component:SettingsPage,
    }
  ],
});