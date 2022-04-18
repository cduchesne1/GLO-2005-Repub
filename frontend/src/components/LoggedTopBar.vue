<template>
  <div class="flex justify-evenly items-center px-24 py-10">
    <div class="flex items-center">
      <img
        @click="goToHome()"
        src="../assets/rePubIcon.svg"
        class="cursor-pointer"
      />
      <search-bar/>
      <a
        @click="goToUserTasks()"
        class="text-base text-gray-500 mr-4 cursor-pointer"
        >Tasks</a
      >
      <a class="text-base text-gray-500">Explore</a>
    </div>
    <ProfilePicture class="cursor-pointer" :path="`/${this.$store.user.username}`" :name="$store.user.name" />
  </div>
</template>
<script>
import ProfilePicture from "@/components/ProfilePicture";
import SearchBar from "@/components/SearchBar";

export default {
  components: {
    SearchBar,
    ProfilePicture,
  },
  methods: {
    goToHome() {
      this.$router.push("/");
    },
    goToUserTasks() {
      this.$router.push({
        path: "/tasks",
      });
    },
  },
};
</script>
