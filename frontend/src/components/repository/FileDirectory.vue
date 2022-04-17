<template>
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
</template>
<script>
import { fetchRepositoryFiles } from "@/api/repositoryApi";

export default {
  data() {
    return {
      allFiles: null,
      folders: [],
      isNested: this.$route.path.includes("/tree/"),
    };
  },
  async created() {
    this.allFiles = await fetchRepositoryFiles(
      this.$route.params.username,
      this.$route.params.repository,
      "master"
    );
    this.getFiles(this.allFiles);
  },
  methods: {
    openDirectory(file) {
      const currentPath = this.$route.params.path;
      console.log(currentPath);
      if (currentPath) {
          if (file.isFolder) {
            this.$router.push(`/${this.$route.params.username}/${this.$route.params.repository}/tree/master/${currentPath}/${file.file}`);
          } else {
            this.$router.push(`/${this.$route.params.username}/${this.$route.params.repository}/blob/master/${currentPath}/${file.file}`);
          }
      } else {
          if (file.isFolder) {
            this.$router.push(`/${this.$route.params.username}/${this.$route.params.repository}/tree/master/${file.file}`);
          } else {
            this.$router.push(`/${this.$route.params.username}/${this.$route.params.repository}/blob/master/${file.file}`);
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
  },
  watch: {
    $route() {
      this.folders = [];
      this.getFiles(this.allFiles);
    },
  },
};
</script>
