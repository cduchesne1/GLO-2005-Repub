<template>
  <div class="flex flex-col mt-16">
    <div v-if="task" class="flex flex-col border-b border-solid border-gray-500 pb-4">
      <div class="flex justify-between w-full">
        <div class="flex items-center">
          <h2 class="text-4xl text-white mr-4">
            {{ task.title }}
          </h2>
          <h2 class="text-4xl text-gray-500">{{ `#${task.number}` }}</h2>
        </div>
        <div class="flex items-center">
          <button
            class="bg-gray-500 hover:bg-gray-600 text-white text-sm font-bold py-1 px-4 rounded mx-4 h-8"
          >
            Edit
          </button>
          <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded h-8 w-24"
            @click="createNewTask()"
          >
            New task
          </button>
        </div>
      </div>
      <div class="flex items-center">
        <div
          class="bg-green-500 rounded-full py-2 px-4 text-white w-16 flex justify-center mr-4"
          :class="task.state == 'closed' ? 'bg-purple-500' : ''"
        >
          {{ task.state.charAt(0).toUpperCase() + task.state.slice(1) }}
        </div>
        <a class="text-gray-500 text-base font-bold mr-2">{{
          task.creator.username
        }}</a>
        <a class="text-gray-500 text-base">{{
          `opened this task ${timeAgo(task.timestamp)} - 0 comments`
        }}</a>
      </div>
    </div>
    <div class="flex">
      <div class="flex flex-col flex-1">
        <div v-if="task" class="border border-solid border-gray-500 rounded-lg w-full mt-4">
          <div class="flex bg-pink-500 bg-opacity-25 px-8 py-4 justify-between">
            <div>
              <a class="text-base text-white font-bold mr-4">{{
                task.creator.username
              }}</a>
              <a class="text-base text-gray-500">{{
                `commented ${timeAgo(task.timestamp)}`
              }}</a>
            </div>
            <a class="text-base text-gray-500 hover:text-pink-500">Edit</a>
          </div>
          <div class="text-white px-4 py-4">
            {{ task.description }}
          </div>
        </div>
        <div class="flex flex-col mt-16">
          <div
            v-for="comment in comments"
            :key="comment.id"
            class="border border-solid border-gray-500 rounded-lg w-full mt-4"
          >
            <div
              class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between"
            >
              <div>
                <a class="text-base text-white font-bold mr-4">{{ comment.sender.username }}</a>
                <a class="text-base text-gray-500">{{ `commented ${timeAgo(comment.timestamp)}` }}</a>
              </div>
              <a class="text-base text-gray-500 hover:text-pink-500">Edit</a>
            </div>
            <div class="text-white px-4 py-4">
              {{ comment.comment }}
            </div>
          </div>
        </div>
      </div>
      <div
        v-if="task"
        class="flex flex-col ml-16 mt-4 border-b border-solid border-gray-500 h-24"
      >
        <div class="flex justify-between w-56">
          <a class="text-base text-gray-500 font-bold">Assignee</a>
          <a class="text-base text-gray-500 hover:text-pink-500 text-right"
            >Add</a
          >
        </div>
        <a v-if="!task.assigned" class="text-base text-gray-500 mt-4">No one - assign yourself</a>
        <a v-if="task.assigned" class="text-base text-gray-500 mt-4">{{ task.assigned }}</a>
      </div>
    </div>
  </div>
</template>
<script>
import moment from "moment";
import {
  fetchTaskByUsernameRepositoryAndNumber,
  fetchTaskComments,
} from "@/api/taskApi";

export default {
  data() {
    return {
      task: null,
      comments: [],
    };
  },
  async created() {
    this.task = await fetchTaskByUsernameRepositoryAndNumber(
      this.$route.params.username,
      this.$route.params.repository,
      this.$route.params.number
    );
    this.comments = await fetchTaskComments(this.task.id);
  },
  methods: {
    createNewTask() {
      this.$router.push(`/${this.$route.params.username}/${this.$route.params.repository}/tasks/new`);
    },
    timeAgo(timestamp) {
      return moment(Date.parse(timestamp)).fromNow();
    },
  },
};
</script>
