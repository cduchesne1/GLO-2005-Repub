<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div>
      <div class="text-center" v-if="isLoading">
        <svg class="inline mr-3 w-8 h-8 text-pink-600 animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
          <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
        </svg>
      </div>
    <div class="flex px-48 justify-between items-center my-16" v-if="!isLoading">
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
      <div v-if="repositories.length <= 0" class="text-xl text-white font-bold mt-32 flex justify-center">
        You don't have any repositories yet. Create one now!
      </div>
      <RepositoryItem
        v-for="repo in repositories"
        :repository="repo"
        :key="repo.owner.username + '-' + repo.name"
      />
    </div>
    <FooterComponent class="mt-auto" />
  </div>
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import RepositoryItem from "@/components/RepositoryItem";
import ProfilePicture from "@/components/ProfilePicture";
import { fetchUserRepositories } from "@/api/repositoryApi";
import { fetchUser } from "@/api/userApi";

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
      isLoading: false,
    };
  },
  async created() {
    this.isLoading = true;
    this.user = await fetchUser(this.$route.params.username);
    this.repositories = await fetchUserRepositories(this.$route.params.username);
    this.isLoading = false;
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
