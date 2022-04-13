<template>
  <div class="flex">
    <div class="flex flex-col items-center mt-16 flex-1">
      <div class="border border-solid border-gray-500 rounded-lg w-full">
        <div
          v-for="(folder, index) in folders"
          :key="folder.name"
          class="border-solid border-gray-500 text-white text-base py-2 px-4"
          :class="index < folders.length - 1 ? 'border-b' : ''"
        >
          {{ folder.name }}
        </div>
      </div>
      <div class="border border-solid border-gray-500 rounded-lg w-full mt-16">
        <div
          class="border-b border-solid border-gray-500 text-white text-base py-2 px-4"
        >
          README.md
        </div>
        <div class="text-white text-base">
          This is where you will find de description of the readme
        </div>
      </div>
    </div>
    <div class="flex flex-col pl-32">
      <div class="border-b border-gray-500 pb-8">
        <a class="text-base text-white font-bold">About</a>
        <p class="text-white text-base max-w-sm text-justify mt-8">
          This is the description of the repository. It goes on and on and on.
        </p>
        <div class="flex items-center mr-4 mt-8">
          <img class="w-6 mr-2" src="@/assets/websiteIcon.svg" />
          <a class="text-sm text-white hover:text-pink-600" href="https://www.google.com"
            >https://www.google.com/</a
          >
        </div>
      </div>
      <div class="flex flex-col border-b border-gray-500 pb-4 pt-8">
        <a class="text-base text-white font-bold">Tags</a>
        <div v-for="tag in tags" :key="tag" class="bg-pink-600 text-white text-xs font-bold py-1 px-1 rounded-xl inline-block mr-auto mt-4">
                {{ tag }}
            </div>
      </div>
      <div class="border-b border-gray-500 pb-4 pt-8">
        <a class="text-base text-white font-bold">Collaborators</a>
        <div class="flex items-center justify-between mr-4 mt-4">
          <img src="@/assets/bigProfilePic.svg" class="w-14"/>
          <img src="@/assets/bigProfilePic.svg" class="w-14"/>
          <img src="@/assets/bigProfilePic.svg" class="w-14"/>
          <img src="@/assets/bigProfilePic.svg" class="w-14"/>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      folders: [
        { name: "folder1" },
        { name: "folder2" },
        { name: "folder3" },
        { name: "folder4" },
        { name: "folder5" },
        { name: "README.md" },
      ],
      tags: ["Java"],
    };
  },
};
</script>
