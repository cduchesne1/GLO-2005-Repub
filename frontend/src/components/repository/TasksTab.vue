<template>
  <div class="flex flex-col items-center mt-16 flex-1">
    <div class="flex justify-end w-full">
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
      >
        New task
      </button>
    </div>
    <div class="border border-solid border-gray-500 rounded-lg w-full mt-4">
      <div class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between">
        <a class="text-base text-white font-bold">24 Tasks</a>
        <a class="text-base text-gray-500">Assignee</a>
      </div>
      <div
        v-for="(task, index) in tasks"
        :key="task"
        class="flex pl-8 pr-10 py-4 justify-between items-center w-full border-solid border-gray-500"
        :class="index < tasks.length - 1 ? 'border-b' : ''"
      >
        <div class="flex flex-col">
          <div class="flex items-center">
            <div class="w-4 h-4 bg-green-500 rounded-full mr-4"></div>
            <h3 class="text-lg font-bold text-white max-w-5xl" @click="onClick()">
              This is the task title
            </h3>
          </div>
          <a class="text-md text-gray-500">#58 opened 14 days ago by johdoe1</a>
        </div>
        <img src="@/assets/profileIcon.svg" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tasks: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    };
  },
  methods: {
    onClick() {
      this.$router.push("/repository/tasks/task");
    },
  },
};
</script>
