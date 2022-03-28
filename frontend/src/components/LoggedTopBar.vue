<template>
  <div class="flex justify-evenly items-center px-24 py-10">
    <div class="flex items-center">
      <img src="../assets/rePubIcon.svg" />
      <input
        type="text"
        v-model="search"
        placeholder="Search"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg mx-4"
      />
      <a class="text-base text-gray-500 mr-4">Tasks</a>
      <a class="text-base text-gray-500">Explore</a>
    </div>
    <img src="../assets/profileIcon.svg" />
  </div>
</template>
