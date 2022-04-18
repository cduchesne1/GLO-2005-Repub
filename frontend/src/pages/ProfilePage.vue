<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex px-48 justify-between items-center my-16">
      <div class="flex">
        <ProfilePicture
          class="cursor-pointer"
          :path="`/${user.username}`"
          :name="user.name"
          :size="48"
        />
        <div class="flex flex-col justify-center ml-4">
          <h1 class="text-5xl text-white font-bold">{{ user.name }}</h1>
          <h2 class="text-pink-600 font-bold text-2xl">{{ user.username }}</h2>
          <div class="flex mt-4">
            <div v-if="user.company" class="flex items-center mr-4">
              <img class="w-7" src="../assets/companyIcon.svg" />
              <a class="text-sm text-white">{{ user.company }}</a>
            </div>
            <div v-if="user.location" class="flex items-center mr-4">
              <img class="w-7" src="../assets/locationIcon.svg" />
              <a class="text-sm text-white">{{ user.location }}</a>
            </div>
            <div v-if="user.website" class="flex items-center mr-4">
              <img class="w-6 mr-2" src="../assets/websiteIcon.svg" />
              <a class="text-sm text-white" href="https://www.google.com">{{
                user.website
              }}</a>
            </div>
          </div>
          <button
            v-if="isCurrentUser()"
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded mx-4 mt-4"
            @click="goToSettings()"
          >
            Edit Profile
          </button>
        </div>
      </div>
      <div v-if="user.bio">
        <h3 class="text-white font-bold text-lg">A little about me:</h3>
        <p class="text-white text-base max-w-sm text-justify">{{ user.bio }}</p>
      </div>
    </div>
    <div class="px-48 flex flex-col">
      <div v-if="isCurrentUser()" class="flex w-full justify-end">
        <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        @click="goToCreationRepository()"
      >
        New
      </button>
      </div>
      <RepositoryItem
        v-for="repo in repositories"
        :repository="repo"
        :key="repo.id"
      />
    </div>
    <FooterComponent class="mt-8" />
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import RepositoryItem from "@/components/RepositoryItem";
import ProfilePicture from "@/components/ProfilePicture";
import { fetchUserByUsername } from "@/api/userApi";
import { fetchUserRepositories } from "@/api/repositoryApi";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
    RepositoryItem,
    ProfilePicture,
  },
  data() {
    return {
      user: null,
      repositories: [],
    };
  },
  async created() {
    this.user = await fetchUserByUsername(this.$route.params.username);
    this.repositories = await fetchUserRepositories(this.user.id);
    console.log(this.repositories);
  },
  methods: {
    goToSettings() {
      this.$router.push("/settings/profile");
    },
    goToCreationRepository() {
      this.$router.push("/new");
    },
    isCurrentUser() {
      return this.user.username === this.$store.user.username;
    },
  },
};
</script>
