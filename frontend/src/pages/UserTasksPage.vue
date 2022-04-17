<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="px-32">
      <div class="border border-solid border-gray-500 rounded-lg w-full mt-4">
        <div class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between">
          <a class="text-base text-white font-bold">{{ `${tasks.length} tasks` }}</a>
        </div>
        <div
          v-for="(task, index) in tasks"
          :key="task.id"
          class="flex pl-8 pr-10 py-4 justify-between items-center w-full border-solid border-gray-500"
          :class="index < tasks.length - 1 ? 'border-b' : ''"
        >
          <div class="flex flex-col">
            <div class="flex items-center">
              <div class="w-4 h-4 bg-green-500 rounded-full mr-4" :class="task.state == 'closed' ? 'bg-purple-500': ''"></div>
              <div class="flex">
                <h3
                  @click="goToRepository(task.repository.owner.username, task.repository.name)"
                  class="text-lg font-bold text-gray-500 max-w-2xl mr-2 cursor-pointer hover:text-pink-600"
                >
                  {{`${task.repository.owner.username}/${task.repository.name}`}}
                </h3>
                <h3
                  @click="goToTask(task.repository.owner.username, task.repository.name, task.number)"
                  class="text-lg font-bold text-white max-w-3xl cursor-pointer hover:text-pink-600"
                >
                  {{ task.title }}
                </h3>
              </div>
            </div>
            <a class="text-md text-gray-500"
              >{{ `#${task.number} opened ${timeAgo(task.timestamp)} by ${task.creator.username}` }}</a
            >
          </div>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>
<script>
import moment from "moment";
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import { fetchUserTasks } from "@/api/taskApi";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
  },
  data() {
    return {
      tasks: [],
    };
  },
  async created() {
    this.tasks = await fetchUserTasks(this.$store.user.id);
  },
  methods: {
    goToTask(username, repository, number) {
      this.$router.push(`/${username}/${repository}/tasks/${number}`);
    },
    goToRepository(username, repository) {
      this.$router.push(`/${username}/${repository}`);
    },
    timeAgo(timestamp) {
      return moment(Date.parse(timestamp)).fromNow();
    },
  },
};
</script>
