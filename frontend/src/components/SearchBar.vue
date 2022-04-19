<template>
  <div class=" flex w-full">
    <div
        class="transform mx-1.5 w-56 lg:w-full max-w-lg"
        :class="isOpen ? 'absolute' : 'hidden'"
    >
      <div class=" pt-10 bg-gray-500 w-96 py-2 px-2 rounded-lg mx-4">
        <a
            class="text-gray-400"
            :class="
            userOptions.length == 0 && repoOptions.length == 0
              ? 'flex mx-2.5 my-1.5'
              : 'hidden'
          "
        >No results</a
        >
        <div id="search-bar-options">
          <a
              class="text-gray-900 font-bold"
              :class="repoOptions.length != 0 ? 'flex mx-2.5 my-1.5' : 'hidden'"
          >Repository</a
          >
          <div v-for="option in repoOptions.slice(0, 4)" :key="option.id">
            <button
                class="flex bg-transparent hover:bg-pink-600 w-full px-1.5 "
                @click="choose(option)"
            >
              {{ option.name }}
            </button>
          </div>
          <a
              class="text-gray-900 font-bold"
              :class="userOptions.length != 0 ? 'flex mx-2.5 my-1.5' : 'hidden'"
          >Users</a
          >
          <div v-for="option in userOptions.slice(0, 4)" :key="option.id">
            <button
                class="flex bg-transparent hover:bg-pink-600 w-full px-1.5"
                @click="choose(option)"
            >
              {{ option.username }}
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full flex flex-col rounded-full">
      <div
          class="relative w-full left-1.5 h-10 rounded-full align-middle "
      >
        <input
            type="text"
            ref="search-bar"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg mx-4 "
            placeholder="Search.."
            v-on:keyup="filterFunction"
        />
        <button
            id="cancel-search-button"
            class="absolute h-full right-5 cursor-pointer"
            v-on:click="clearData"
        >
          <svg
              class="h-4 w-4"
              viewBox="0 0 24 24"
              fill="none"
              stroke="gray"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
          >
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>

import {fetchRepositoryByText} from "@/api/repositoryApi";
import {fetchUsersByText} from "@/api/userApi";

export default {
  name: "SearchBar",
  data() {
    return {
      isOpen: false,
      options: [],
      repoOptions: [],
      userOptions: [],
    };
  },
  methods: {
    async filterFunction() {
      let input, filter;
      input = this.$refs["search-bar"];
      filter = input.value.toLowerCase();
      this.repoOptions = await fetchRepositoryByText(filter);
      this.userOptions = await fetchUsersByText(filter);
      this.isOpen = true;
    },
    clearData() {
      this.$refs["search-bar"].value = "";
      this.isOpen = false;
    },
    choose(option) {
      this.$refs["search-bar"].value = option.name;
      this.userOptions = [];
      this.restoOptions = [];
      this.isOpen = false;
      if (option.visibility) {
        this.$router.push({ path: "/" + option.owner.username + "/" + option.name });
      } else {
        this.$router.push({ path: "/" + option.username });
      }
    },
  },
};
</script>
