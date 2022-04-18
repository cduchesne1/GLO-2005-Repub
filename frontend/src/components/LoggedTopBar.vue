<template>
  <div class="flex justify-evenly items-center px-24 py-10">
    <div class="flex items-center">
      <img
        @click="goToHome()"
        src="../assets/rePubIcon.svg"
        class="cursor-pointer"
      />
      <input
        type="text"
        placeholder="Search"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg mx-4"
      />
      <a
        @click="goToUserTasks()"
        class="text-base text-gray-500 mr-4 cursor-pointer"
        >Tasks</a
      >
      <a class="text-base text-gray-500"
         @click="goToUserExplore()"
      >Explore</a>
    </div>
    <ProfilePicture v-if="$store.isConnected"
    class="cursor-pointer"
    :path="`/${this.$store.user.username}`" 
    :name="$store.user.name" />
    <div v-if="!$store.isConnected" class="flex items-center">
      <a class="text-base text-gray-500">Explore</a>
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
import ProfilePicture from "@/components/ProfilePicture";

export default {
  components: {
    ProfilePicture,
  },
  methods: {
    goToHome() {
      if (this.$store.isConnected){
        this.$router.push("/logged");
      } else {
        this.$router.push("/");
      }
    },
    goToUserTasks() {
      this.$router.push({
        path: "/tasks",
      });
    },
    goToLogin() {
      this.$router.push("/login");
    },
    goToSignUp() {
      this.$router.push("/signup");
    },
    goToUserExplore() {
      this.$router.push({
        path: "/loggedExplore",
      });
    },
  },
};
</script>
