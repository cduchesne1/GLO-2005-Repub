<template>
  <div class="flex flex-col w-full">
    <div v-if="!isNested" class="flex justify-between mb-8">
      <v-select
        :options="branches"
        :value="selectedBranch"
        @input="switchBranch"
        class="branch-picker w-48"
      >
      </v-select>
      <div class="flex items-center">
        <input
          type="text"
          readonly
          ref="path"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg h-10"
          :value="repositoryPath"
        />
        <button
          v-clipboard="repositoryPath"
          v-clipboard:success="clipboardSuccessHandler"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4 h-8"
        >
          Copy
        </button>
      </div>
    </div>
    <div
      class="border border-solid border-gray-500 rounded-lg w-full"
      :class="isNested ? 'mt-16' : ''"
    >
      <div
        v-for="(file, index) in folders"
        :key="index"
        class="border-solid border-gray-500 text-white text-base py-2 px-4 flex items-center"
        :class="index < Object.keys(allFiles).length - 1 ? 'border-b' : ''"
      >
        <img v-if="!file.isFolder" src="@/assets/fileIcon.svg" class="w-6" />
        <img v-if="file.isFolder" src="@/assets/folderIcon.svg" class="w-6" />
        <a
          @click="openDirectory(file)"
          class="ml-2 cursor-pointer hover:text-pink-600"
          >{{ file.file }}</a
        >
      </div>
    </div>
  </div>
</template>
<script>
import {
  fetchRepositoryFiles,
  fetchRepositoryBranches,
} from "@/api/repositoryApi";

export default {
  data() {
    return {
      allFiles: null,
      folders: [],
      branches: [],
      selectedBranch: null,
      isNested: this.$route.path.includes("/tree/"),
      repositoryPath: `http://localhost:8000/${this.$route.params.username}/${this.$route.params.repository}.git`,
    };
  },
  async created() {
    this.branches = await fetchRepositoryBranches(
      this.$route.params.username,
      this.$route.params.repository
    );

    if (this.$route.params.branch) {
      this.selectedBranch = this.$route.params.branch;
    } else {
      if (!this.selectedBranch) {
        this.selectedBranch = this.branches[0];
      }
    }

    this.allFiles = await fetchRepositoryFiles(
      this.$route.params.username,
      this.$route.params.repository,
      this.selectedBranch
    );
    this.getFiles(this.allFiles);
  },
  methods: {
    async switchBranch(value) {
      if (value !== this.selectedBranch) {
        this.selectedBranch = value;
        this.allFiles = await fetchRepositoryFiles(
          this.$route.params.username,
          this.$route.params.repository,
          this.selectedBranch
        );
        this.folders = [];
        this.getFiles(this.allFiles);
      }
    },
    openDirectory(file) {
      const currentPath = this.$route.params.path;
      if (currentPath) {
        if (file.isFolder) {
          this.$router.push(
            `/${this.$route.params.username}/${this.$route.params.repository}/tree/${this.selectedBranch}/${currentPath}/${file.file}`
          );
        } else {
          this.$router.push(
            `/${this.$route.params.username}/${this.$route.params.repository}/blob/${this.selectedBranch}/${currentPath}/${file.file}`
          );
        }
      } else {
        if (file.isFolder) {
          this.$router.push(
            `/${this.$route.params.username}/${this.$route.params.repository}/tree/${this.selectedBranch}/${file.file}`
          );
        } else {
          this.$router.push(
            `/${this.$route.params.username}/${this.$route.params.repository}/blob/${this.selectedBranch}/${file.file}`
          );
        }
      }
    },
    getFiles(files) {
      files
        .filter((file) => {
          let isFolder = false;
          if (this.$route.params.path) {
            if (file.includes(this.$route.params.path)) {
              if (
                file.replace(`${this.$route.params.path}/`, "").split("/")
                  .length > 1
              ) {
                isFolder = true;
              }
              this.folders.push({
                file: file
                  .replace(`${this.$route.params.path}/`, "")
                  .split("/")[0],
                isFolder,
              });
            }
          } else {
            if (file.split("/").length > 1) {
              isFolder = true;
            }
            this.folders.push({ file: file.split("/")[0], isFolder });
          }
        })
        .forEach((file) => {
          this.folders.push(file.path);
        });
      this.folders.sort((a, b) =>
        a.file.toLowerCase() > b.file.toLowerCase()
          ? 1
          : b.file.toLowerCase() > a.file.toLowerCase()
          ? -1
          : 0
      );
    },
    clipboardSuccessHandler() {
      alert("Copied to clipboard");
    },
  },
  watch: {
    $route() {
      this.folders = [];
      this.getFiles(this.allFiles);
    },
  },
};
</script>
<style scoped>
.branch-picker {
  --vs-controls-color: #eeeeee;
  --vs-border-color: rgba(107, 114, 128, 1);

  --vs-dropdown-bg: rgba(17, 24, 39, 1);
  --vs-dropdown-color: #eeeeee;
  --vs-dropdown-option-color: #eeeeee;

  --vs-selected-bg: rgba(219, 39, 119, 1);
  --vs-selected-color: #eeeeee;

  --vs-search-input-color: #eeeeee;

  --vs-dropdown-option--active-bg: rgba(219, 39, 119, 1);
  --vs-dropdown-option--active-color: #eeeeee;
}
</style>
