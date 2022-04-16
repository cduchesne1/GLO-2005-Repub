<template>
  <div class="flex flex-col items-center mt-16 flex-1">
    <div class="flex justify-end w-full">
      <button
        @click="createNewTask()"
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
      >
        New task
      </button>
    </div>
    <div class="border border-solid border-gray-500 rounded-lg w-full mt-4">
      <div class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between">
        <a class="text-base text-white font-bold">{{ `${tasks.length} tasks` }}</a>
        <a class="text-base text-gray-500">Assignee</a>
      </div>
      <div
        v-for="(task, index) in tasks"
        :key="task.id"
        class="flex pl-8 pr-10 py-4 justify-between items-center w-full border-solid border-gray-500"
        :class="index < tasks.length - 1 ? 'border-b' : ''"
      >
        <div class="flex flex-col">
          <div class="flex items-center">
            <div class="w-4 h-4 rounded-full bg-green-500 mr-4" :class="task.state == 'closed' ? 'bg-purple-500': ''"></div>
            <h3
              class="text-lg font-bold text-white max-w-5xl"
              @click="onClick()"
            >
              {{ task.title }}
            </h3>
          </div>
          <a class="text-md text-gray-500">{{ `#${task.number} opened ${timeAgo(task.timestamp)} by ${task.creator.username}` }}</a>
        </div>
        <ProfilePicture
        v-if="task.assigned"
            class="cursor-pointer"
            :path="`/${task.assigned.username}`"
            :name="task.assigned.name"
          />
      </div>
    </div>
  </div>
</template>
<script>
import moment from "moment";
import { fetchRepositoryByUsernameAndName } from "@/api/repositoryApi";
import { fetchRepositoryTasks } from "@/api/taskApi";

export default {
  data() {
    return {
      repository: null,
      tasks: [],
    };
  },
  async created() {
    this.repository = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    );
    this.tasks = await fetchRepositoryTasks(this.repository.id);
  },
  methods: {
    onClick() {
      this.$router.push("/repository/tasks/task");
    },
    createNewTask() {
      this.$router.push("/repository/tasks/new");
    },
    timeAgo(timestamp) {
      return moment(Date.parse(timestamp)).fromNow();
    },
  },
};
</script>
