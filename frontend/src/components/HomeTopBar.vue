<template>
  <div class="flex justify-evenly items-center px-24 py-10">
    <div class="flex">
      <img src="../assets/rePubIcon.svg" />
      <h2 class="text-white font-bold text-lg ml-4">RePub</h2>
    </div>
    <search-bar/>
    <div class="flex items-center">
      <a class="text-base text-gray-500">Explore</a>
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded mx-4"
      >
        Sign Up
      </button>
      <button
        class="border-pink-600 hover:border-pink-700 hover:text-pink-700 text-pink-600 text-sm font-bold py-2 px-8 border-2 border-solid rounded"
      >
        Sign In
      </button>
    </div>
  </div>
</template>
<script>
import SearchBar from "@/components/SearchBar";
export default {
  components: {SearchBar}
}
</script>