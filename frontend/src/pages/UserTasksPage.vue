<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="px-32">
      <div class="border border-solid border-gray-500 rounded-lg w-full mt-4">
        <div class="flex bg-gray-500 bg-opacity-25 px-8 py-4 justify-between">
          <a class="text-base text-white font-bold">24 Tasks</a>
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
              <div class="flex">
                <h3 class="text-lg font-bold text-gray-500 max-w-2xl mr-2">
                  johndoe1/hello
                </h3>
                <h3 class="text-lg font-bold text-white max-w-3xl">
                  This is the task title
                </h3>
              </div>
            </div>
            <a class="text-md text-gray-500"
              >#58 opened 14 days ago by johdoe1</a
            >
          </div>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
  },
  data() {
    return {
      tasks: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    };
  },
};
</script>
