<template>
  <div class="flex flex-col mt-16">
    <div class="flex flex-col border-b border-solid border-gray-500 pb-4">
      <div class="flex justify-between w-full">
        <div class="flex items-center">
          <h2 class="text-4xl text-white mr-4">
            This is the title of the task
          </h2>
          <h2 class="text-4xl text-gray-500">#32</h2>
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
        >
          Open
        </div>
        <a class="text-gray-500 text-base font-bold mr-2">johndoe1</a>
        <a class="text-gray-500 text-base"
          >opened this issue 15 days ago - 0 comments</a
        >
      </div>
    </div>
    <div class="flex">
      <div class="flex flex-col flex-1">
        <div class="border border-solid border-gray-500 rounded-lg w-full mt-4">
          <div class="flex bg-pink-500 bg-opacity-25 px-8 py-4 justify-between">
            <div>
              <a class="text-base text-white font-bold mr-4">johndoe1</a>
              <a class="text-base text-gray-500">commented 10 days ago</a>
            </div>
            <a class="text-base text-gray-500 hover:text-pink-500">Edit</a>
          </div>
          <div class="text-white max-w-5xl px-4 py-4">
            This is the content of the comment. There is some amazing stuff in
            here yolo.
          </div>
        </div>
        <div class="flex flex-col mt-16">
          <div
            class="border border-solid border-gray-500 rounded-lg w-full mt-4"
          >
            <div
              class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between"
            >
              <div>
                <a class="text-base text-white font-bold mr-4">johndoe1</a>
                <a class="text-base text-gray-500">commented 10 days ago</a>
              </div>
              <a class="text-base text-gray-500 hover:text-pink-500">Edit</a>
            </div>
            <div class="text-white max-w-5xl px-4 py-4">
              This is the content of the comment. There is some amazing stuff in
              here yolo.
            </div>
          </div>
        </div>
      </div>
      <div
        class="flex flex-col ml-16 mt-4 border-b border-solid border-gray-500 h-24"
      >
        <div class="flex justify-between w-56">
          <a class="text-base text-gray-500 font-bold">Assignee</a>
          <a class="text-base text-gray-500 hover:text-pink-500 text-right"
            >Add</a
          >
        </div>
        <a class="text-base text-gray-500 mt-4">No one - assign yourself</a>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    createNewTask() {
      this.$router.push("/repository/tasks/new");
    },
  },
};
</script>
