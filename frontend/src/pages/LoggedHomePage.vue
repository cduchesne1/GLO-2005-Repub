<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex justify-center flex-1">
      <div class="flex flex-col px-16 pt-8 bg-gray-900">
        <div
          class="flex items-center border-b border-solid border-gray-500 pb-8"
        >
          <ProfilePicture class="cursor-pointer" :action="goToProfile" :name="$store.user.name" />
          <a
            @click="goToProfile()"
            class="text-base text-white font-bold ml-4 cursor-pointer hover:text-pink-600"
            >{{ $store.user.username }}</a
          >
        </div>
        <div class="flex flex-col mt-8">
          <div class="flex items-center mb-4">
            <a class="text-base text-white font-bold">Recent Repositories</a>
            <button
              class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
              @click="goToCreationRepository()"
            >
              New
            </button>
          </div>
          <a
            v-for="repo in recentRepositories"
            :key="repo.id"
            @click="goToRepository(repo.owner.username, repo.name)"
            class="text-base text-white mt-2 cursor-pointer hover:text-pink-600"
          >
            {{ `${repo.owner.username}/${repo.name}` }}
          </a>
        </div>
      </div>
      <div class="flex flex-col flex-1 pt-8 items-center">
        <p class="text-base text-white font-bold">
          {{ `Hi ${$store.user.name.split(' ')[0]}, there is no news for you!` }}
        </p>
        <FooterComponent class="mt-auto" />
      </div>
      <div class="flex flex-col pr-48 pt-8">
        <a class="text-base text-white font-bold">Explore Repositories</a>
        <div
          v-for="repo in exploreRepositories"
          :key="repo.id"
          class="flex flex-col border-b border-solid border-gray-500 mt-8"
        >
          <a
            @click="goToRepository(repo.owner.username, repo.name)"
            class="text-base text-white mt-2 cursor-pointer hover:text-pink-600"
            >{{ `${repo.owner.username}/${repo.name}` }}</a
          >
          <div
            v-for="tag in repo.tags"
            :key="tag"
            class="bg-pink-600 text-white text-xs font-bold py-1 px-1 rounded-xl inline-block mr-auto my-2"
          >
            {{ tag }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import ProfilePicture from "@/components/ProfilePicture";
import { fetchUserRecentRepositories, fetchExploreRepositories } from "@/api/repositoryApi";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
    ProfilePicture,
  },
  data() {
    return {
      recentRepositories: [],
      exploreRepositories: [],
    };
  },
  async created () {
      this.recentRepositories = await fetchUserRecentRepositories(this.$store.user.id);
      this.exploreRepositories = (await fetchExploreRepositories()).slice(0, 5);
  },
  methods: {
    goToCreationRepository() {
      this.$router.push("/new");
    },
    goToRepository(username, repository) {
      this.$router.push(`/${username}/${repository}`);
    },
    goToProfile() {
      this.$router.push(`/${this.$store.user.username}`);
    },
  },
};
</script>
