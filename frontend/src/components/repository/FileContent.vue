<template>
  <div class="border border-solid border-gray-500 rounded-lg w-full mt-16">
    <div
      class="border-b border-solid border-gray-500 text-white text-base py-2 px-4"
    >
      {{ fileName }}
    </div>
    <div id="content" class="text-white text-base px-4 py-4"></div>
  </div>
</template>
<script>
import { marked } from "marked";
import { fetchFileContent } from "@/api/repositoryApi";

export default {
  data() {
    return {
      file: null,
      fileName: "",
    };
  },
  async created() {
    this.fileName = this.$route.params.path.split("/").pop();
    this.file = await fetchFileContent(
      this.$route.params.username,
      this.$route.params.repository,
      this.$route.params.path,
      this.$route.params.branch
    );
    if (this.fileName.includes(".md")) {
      document.getElementById("content").innerHTML = marked.parse(this.file);
    } else {
        document.getElementById("content").innerHTML = this.file;
        document.getElementById("content").classList.add("whitespace-pre-wrap");
    }
  },
};
</script>
