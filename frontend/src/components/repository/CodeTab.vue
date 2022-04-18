<template>
  <div>
    <div class="text-center" v-if="isLoading">
      <svg class="inline mr-3 w-8 h-8 text-pink-600 animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
        <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
      </svg>
    </div>
  <div class="flex" v-if="!isLoading">
    <div v-if="files.length <= 0" class="flex flex-col items-center mt-16 flex-1">
      <div class="border border-solid border-gray-500 rounded-lg w-full">
        <div
          class="flex flex-col border border-solid border-gray-500 bg-pink-600 bg-opacity-25 rounded-lg w-full px-4 py-4"
        >
          <h2 class="text-white text-2xl font-bold">Quick setup</h2>
          <div class="flex">
            <input
              type="text"
              readonly
              ref="path"
              class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
              :value="repositoryPath"
            />
            <button
              v-clipboard="repositoryPath"
              v-clipboard:success="clipboardSuccessHandler"
              class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
            >
              Copy
            </button>
          </div>
        </div>
        <div class="flex flex-col text-white text-base px-4 py-4">
          <h2 class="text-white text-2xl font-bold">
            ...or create a new repository on the command line
          </h2>
          <textarea
            type="text"
            readonly
            class="bg-gray-900 text-white w-full h-48 py-2 px-2 rounded-lg mt-4"
            :value="createRepoText"
          />

          <h2 class="text-white text-2xl font-bold mt-4">
            …or push an existing repository from the command line
          </h2>
          <textarea
            type="text"
            readonly
            class="bg-gray-900 text-white w-full h-24 py-2 px-2 rounded-lg mt-4"
            :value="pushRepoText"
          />
        </div>
      </div>
    </div>
    <div v-if="files.length > 0" class="flex flex-col items-center mt-16 flex-1">
      <router-view></router-view>
      <div class="border border-solid border-gray-500 rounded-lg w-full mt-16">
        <div
          v-if="hasReadme"
          class="border-b border-solid border-gray-500 text-white text-base py-2 px-4"
        >
          README.md
        </div>
        <div id="readme" class="text-white text-base px-4 py-4 whitespace-pre-wrap"></div>
      </div>
    </div>
    <div class="flex flex-col pl-32">
      <div class="border-b border-gray-500 pb-8">
        <a class="text-base text-white font-bold">About</a>
        <p
          v-if="repository && repository.description"
          class="text-white text-base max-w-sm text-justify mt-8"
        >
          {{ repository.description }}
        </p>
        <div class="flex items-center mr-4 mt-8">
          <img
            v-if="repository && repository.website"
            class="w-6 mr-2"
            src="@/assets/websiteIcon.svg"
          />
          <a
            v-if="repository && repository.website"
            class="text-sm text-white hover:text-pink-600"
            href="https://www.google.com"
            >{{ repository.website }}</a
          >
        </div>
      </div>
      <div class="flex flex-col border-b border-gray-500 pb-4 pt-8">
        <a class="text-base text-white font-bold">Tags</a>
        <div v-if="repository && repository.tags">
          <div
            v-for="tag in repository.tags"
            :key="tag"
            class="bg-pink-600 text-white text-xs font-bold py-1 px-1 rounded-xl inline-block mr-auto mt-4"
          >
            {{ tag }}
          </div>
        </div>
      </div>
      <div class="border-b border-gray-500 pb-4 pt-8">
        <a class="text-base text-white font-bold">Collaborators</a>
        <div
          v-if="repository && repository.collaborators"
          class="flex items-center justify-between mr-4 mt-4"
        >
          <ProfilePicture
            v-for="collaborator in repository.collaborators"
            :key="collaborator.id"
            class="cursor-pointer"
            :size="14"
            :path="`/${collaborator.username}`"
            :name="collaborator.name"
          />
        </div>
      </div>
    </div>
  </div>
  </div>
</template>
<script>
import ProfilePicture from "@/components/ProfilePicture";
import { marked } from "marked";
import {
  fetchRepositoryByUsernameAndName,
  fetchRepositoryFiles,
  fetchFileContent,
} from "@/api/repositoryApi";

export default {
  components: { ProfilePicture },
  data() {
    return {
      repository: null,
      files: null,
      hasReadme: false,
      repositoryPath: `http://localhost:8000/${this.$route.params.username}/${this.$route.params.repository}.git`,
      createRepoText: `echo "# ${this.$route.params.repository}" >> README.md\ngit init\ngit add README.md\ngit commit -m "first commit"\ngit branch -M master\ngit remote add origin http://localhost:8000/${this.$route.params.username}/${this.$route.params.repository}.git\ngit push -u origin master`,
      pushRepoText: `git remote add origin http://localhost:8000/${this.$route.params.username}/${this.$route.params.repository}.git\ngit branch -M master\ngit push -u origin master`,
    };
  },
  computed: {},
  async created() {
    this.repository = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    );
    this.files = await fetchRepositoryFiles(
      this.$route.params.username,
      this.$route.params.repository,
      "master"
    );

    if (this.files.includes("README.md")) {
      const data = await fetchFileContent(
        this.$route.params.username,
        this.$route.params.repository,
        "README.md",
        "master"
      );
      this.isLoading = false;
      this.hasReadme = true;
      document.getElementById("readme").innerHTML = marked.parse(data);
    }
  },
  methods: {
    goToProfile(username) {
      this.$router.push(`/${username}`);
    },
    clipboardSuccessHandler() {
      alert("Copied to clipboard");
    },
  },
};
</script>
