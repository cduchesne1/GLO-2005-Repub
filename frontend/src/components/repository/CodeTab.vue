<template>
  <div class="flex">
    <div class="flex flex-col items-center mt-16 flex-1">
      <div class="border border-solid border-gray-500 rounded-lg w-full">
        <div
          v-for="(folder, index) in folders"
          :key="folder.name"
          class="border-solid border-gray-500 text-white text-base py-2 px-4"
          :class="index < folders.length - 1 ? 'border-b' : ''"
        >
          {{ folder.name }}
        </div>
      </div>
      <div class="border border-solid border-gray-500 rounded-lg w-full mt-16">
        <div
          class="border-b border-solid border-gray-500 text-white text-base py-2 px-4"
        >
          README.md
        </div>
        <div class="text-white text-base">
          This is where you will find de description of the readme
        </div>
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
        <div v-if="repository && repository.collaborators" class="flex items-center justify-between mr-4 mt-4">
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
import { fetchRepositoryByUsernameAndName } from "@/api/repositoryApi";

export default {
  components: { ProfilePicture },
  data() {
    return {
      repository: null,
      folders: [
        { name: "folder1" },
        { name: "folder2" },
        { name: "folder3" },
        { name: "folder4" },
        { name: "folder5" },
        { name: "README.md" },
      ],
      tags: ["Java"],
    };
  },
  async created() {
    this.repository = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    );
  },
  methods: {
    goToProfile(username) {
      this.$router.push(`/${username}`);
    },
  },
};
</script>
