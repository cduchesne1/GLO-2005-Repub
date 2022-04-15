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
        v-model="search"
        placeholder="Search"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg mx-4"
      />
      <a
        @click="goToUserTasks()"
        class="text-base text-gray-500 mr-4 cursor-pointer"
        >Tasks</a
      >
      <a class="text-base text-gray-500">Explore</a>
    </div>
    <ProfilePicture class="cursor-pointer" :action="goToProfile" :name="$store.user.name" />
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
      this.$router.push("/");
    },
    goToProfile() {
      this.$router.push(`/${this.$store.user.username}`);
    },
    goToUserTasks() {
      this.$router.push({
        path: "/tasks",
      });
    },
  },
};
</script>
