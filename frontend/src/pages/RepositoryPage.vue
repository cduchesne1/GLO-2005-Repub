<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex flex-col flex-1 px-16">
      <div class="flex items-center">
        <h1 class="text-2xl text-pink-600">{{ repositoryData.owner.username }}</h1>
        <h1 class="text-2xl text-gray-500 mx-2">/</h1>
        <h1 class="text-2xl text-pink-600 font-bold">{{ repositoryData.name }}</h1>
        <div
          class="border-gray-500 text-gray-500 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid inline-block mr-auto my-2 ml-4"
        >
          {{ repositoryData.visibility.charAt(0).toUpperCase() + repositoryData.visibility.slice(1) }}
        </div>
      </div>
      <TabsComponent class="mt-8">
        <TabComponent
          name="Code"
          :selected="$route.name == 'Code'"
          :href="`#/${repositoryData.owner.username}/${repositoryData.name}`"
        >
        </TabComponent>
        <TabComponent
          name="Tasks"
          :selected="
            $route.name == 'Repository Tasks' || $route.name == 'Single Task'
          "
          :href="`#/${repositoryData.owner.username}/${repositoryData.name}/tasks`"
        >
        </TabComponent>
        <TabComponent
          name="Settings"
          :selected="$route.name == 'Repository Settings'"
          :href="`#/${repositoryData.owner.username}/${repositoryData.name}/settings`"
        >
        </TabComponent>
      </TabsComponent>
      <router-view></router-view>
    </div>
    <FooterComponent />
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import TabsComponent from "@/components/TabsComponent";
import TabComponent from "@/components/TabComponent";
import { fetchRepositoryByUsernameAndName } from "@/api/repositoryApi";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
    TabsComponent,
    TabComponent,
  },
  props: {
    username: {
      type: String,
    },
    repository: {
      type: String,
    },
  },
  data() {
    return {
        repositoryData: null,
    };
  },
  async created() {
    this.repositoryData = await fetchRepositoryByUsernameAndName(this.username, this.repository);
  },
};
</script>
