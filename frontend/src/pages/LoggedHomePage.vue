<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div>
      <div class="text-center" v-if="isLoading">
        <svg
          class="inline mr-3 w-8 h-8 text-pink-600 animate-spin"
          viewBox="0 0 100 101"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
            fill="#E5E7EB"
          />
          <path
            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
            fill="currentColor"
          />
        </svg>
      </div>
      <div class="flex justify-center flex-1 h-full" v-if="!isLoading">
        <div class="flex flex-col px-16 pt-8 bg-gray-900">
          <div
            class="flex items-center border-b border-solid border-gray-500 pb-8"
          >
            <ProfilePicture
              class="cursor-pointer"
              :path="`/${this.$store.user.username}`"
              :name="$store.user.name"
            />
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
              :key="repo.owner + '-' + repo.name"
              @click="goToRepository(repo.owner.username, repo.name)"
              class="text-base text-white mt-2 cursor-pointer hover:text-pink-600"
            >
              {{ `${repo.owner.username}/${repo.name}` }}
            </a>
          </div>
        </div>
        <div class="flex flex-col flex-1 pt-8 items-center justify-between">
          <p class="text-base text-white font-bold">
            {{
              `Hi ${$store.user.name.split(" ")[0]}, there is no news for you!`
            }}
          </p>
          <FooterComponent class="mt-auto" />
        </div>
        <div class="flex flex-col pr-48 pt-8">
          <a class="text-base text-white font-bold">Explore Repositories</a>
          <div
            v-for="repo in exploreRepositories"
            :key="repo.owner + '-' + repo.name"
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
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import ProfilePicture from "@/components/ProfilePicture";
import {
  fetchUserRecentRepositories,
  fetchExploreRepositories,
} from "@/api/repositoryApi";

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
      isLoading: false,
    };
  },
  async created() {
    this.isLoading = true;
    if (!this.$store.isConnected) {
      this.$router.push("/");
    }
    this.recentRepositories = await fetchUserRecentRepositories(
      this.$store.user.username
    );
    this.exploreRepositories = (await fetchExploreRepositories()).slice(0, 5);
    this.isLoading = false;
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
