<template>
  <div
    class="flex flex-col border border-solid border-gray-500 rounded-lg px-4 py-4 mx-48 mt-16"
  >
    <input
      v-model="title"
      type="text"
      class="bg-gray-900 text-white py-2 px-2 rounded-lg"
      placeholder="Title"
    />
    <a v-if="titleError" class="text-md text-red-600 mb-2">{{ titleError }}</a>
    <textarea
      v-model="description"
      type="text"
      class="bg-gray-900 text-white h-48 py-2 px-2 rounded-lg mt-8"
      placeholder="Leave a comment"
    />
    <div class="flex justify-end mt-4">
      <button
        @click="submitTask()"
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded"
      >
        Submit new task
      </button>
    </div>
  </div>
</template>
<script>
import { fetchRepositoryByUsernameAndName } from "@/api/repositoryApi";
import { createTask } from "@/api/taskApi";

export default {
  data() {
    return {
      repository: null,
      title: "",
      description: "",
      titleError: null,
    };
  },
  async created() {
    this.repository = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    );
  },
  methods: {
    async submitTask() {
      if (this.title.length === 0) {
        this.titleError = "Title is required";
        return;
      }
      await createTask({
        repository: this.repository.id,
        creator: this.$store.user.id,
        title: this.title,
        description: this.description ? this.description : null,
      });
      this.$router.back();
    },
  },
};
</script>
