import Vue from "vue";
import Router from "vue-router";
import LoggedHomePage from "@/pages/LoggedHomePage";
import LoginPage from "@/pages/LoginPage";
import SignUp from "@/pages/SignUp";
import ProfilePage from "@/pages/ProfilePage";
import RepositoryPage from "@/pages/RepositoryPage";
import UserTasksPage from "@/pages/UserTasksPage";
import CodeTab from "@/components/repository/CodeTab";
import TasksTab from "@/components/repository/TasksTab";
import SingleTaskTab from "@/components/repository/SingleTaskTab";
import SettingsTab from "@/components/repository/SettingsTab";
import CreateTaskTab from "@/components/repository/CreateTaskTab";
import CreationRepositoryPage from "@/pages/CreationRepositoryPage";
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
      path: "/tasks",
      name: "Tasks",
      component: UserTasksPage,
    },
    {
      path: "/settings",
      name: "Settings",
      component:SettingsPage,
    },
    {
      path:"/settings/profile",
      name: "SettingsProfile",
      component:SettingsPage,
    },
    {
      path: "/new",
      name: "NewRepository",
      component: CreationRepositoryPage,
    },
    {
        path: "/:username",
        name: "Profile",
        component: ProfilePage,
    },
    {
      path: "/:username/:repository",
      name: "Repository",
      component: RepositoryPage,
      props: true,
      children: [
        {
          path: "/:username/:repository",
          name: "Code",
          component: CodeTab,
        },
        {
          path: "/:username/:repository/tasks",
          name: "Repository Tasks",
          component: TasksTab,
        },
        {
          path: "/:username/:repository/tasks/new",
          name: "New Task",
          component: CreateTaskTab,
        },
        {
          path: "/:username/:repository/tasks/:number",
          name: "Single Task",
          component: SingleTaskTab,
        },
        {
          path: "/:username/:repository/settings",
          name: "Repository Settings",
          component: SettingsTab,
        },
      ]
    }
  ],
});