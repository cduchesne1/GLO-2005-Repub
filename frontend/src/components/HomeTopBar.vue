<template>
  <div class="flex justify-evenly items-center px-24 py-10">
    <div class="flex">
      <img
        @click="goToHome()"
        src="../assets/rePubIcon.svg"
        class="cursor-pointer"
      />
      <h2 class="text-white font-bold text-lg ml-4">RePub</h2>
    </div>
    <input
      type="text"
      v-model="search"
      placeholder="Search"
      class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
    />
    <div class="flex items-center">
      <a class="text-base text-gray-500" @click="goToExplore()" >Explore</a>
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded mx-4"
        @click="goToSignUp"
      >
        Sign Up
      </button>
      <button
        class="border-pink-600 hover:border-pink-700 hover:text-pink-700 text-pink-600 text-sm font-bold py-2 px-8 border-2 border-solid rounded"
        @click="goToLogin"
      >
        Sign In
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      search: ""
    }
  },
  methods: {
    goToLogin() {
      this.$router.push("/login");
    },
    goToSignUp() {
      this.$router.push("/signup");
    },
    goToHome() {
      if (this.$store.isConnected){
        this.$router.push("/logged");
      } else {
        this.$router.push("/");
      }
    },
    goToExplore() {
      this.$router.push({
        path: "/explore",
      });
    },
  },
}
</script>
