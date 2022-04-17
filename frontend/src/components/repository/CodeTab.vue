<template>
  <div class="flex">
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
        <div id="readme" class="text-white text-base px-4 py-4"></div>
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
      pushRepoText: `git remote add origin http://localhost:8000/${this.$route.params.username}/${this.$route.params.repository}.git\ngit branch -M master\ngit push -u origin master`
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
