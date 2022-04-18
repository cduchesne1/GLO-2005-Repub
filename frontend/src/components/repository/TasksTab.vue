<template>
  <div>
    <div class="text-center" v-if="isLoading">
      <svg class="inline mr-3 w-8 h-8 text-pink-600 animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
        <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
      </svg>
    </div>
  <div class="flex flex-col items-center mt-16 flex-1" v-if="!isLoading">
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
        <a class="text-base text-white font-bold">{{
          `${tasks.length} tasks`
        }}</a>
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
            <div
              class="w-4 h-4 rounded-full bg-green-500 mr-4"
              :class="task.state == 'closed' ? 'bg-purple-500' : ''"
            ></div>
            <h3
              class="text-lg font-bold text-white max-w-5xl cursor-pointer hover:text-pink-600"
              @click="onClick(task.number)"
            >
              {{ task.title }}
            </h3>
          </div>
          <a class="text-md text-gray-500">{{
            `#${task.number} opened ${timeAgo(task.timestamp)} by ${
              task.creator.username
            }`
          }}</a>
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
  </div>
</template>
<script>
import moment from "moment";
import { fetchRepositoryByUsernameAndName } from "@/api/repositoryApi";
import { fetchRepositoryTasks } from "@/api/taskApi";
import ProfilePicture from "@/components/ProfilePicture";

export default {
  components: {
    ProfilePicture,
  },
  data() {
    return {
      repository: null,
      tasks: [],
      isLoading: false
    };
  },
  async created() {
    this.isLoading = true;
    this.repository = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    );
    this.tasks = await fetchRepositoryTasks(this.repository.id);
    this.isLoading = false;
  },
  methods: {
    onClick(number) {
      this.$router.push(
        `/${this.$route.params.username}/${this.$route.params.repository}/tasks/${number}`
      );
    },
    createNewTask() {
      this.$router.push(
        `/${this.$route.params.username}/${this.$route.params.repository}/tasks/new`
      );
    },
    timeAgo(timestamp) {
      return moment(Date.parse(timestamp)).fromNow();
    },
  },
};
</script>
