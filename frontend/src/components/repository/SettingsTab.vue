<template>
  <div class="flex flex-col w-full px-48 mt-16">
    <div class="border-b border-solid- border-gray-500 w-full pb-4">
      <h2 class="text-3xl text-white">General</h2>
    </div>
    <label class="text-md text-white mt-8 mb-2">Description</label>
    <div class="flex items-end">
      <textarea
        v-model="description"
        type="text"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        :placeholder="
          repository.description
            ? repository.description
            : 'Enter a description...'
        "
      />
      <button
        @click="updateDescription()"
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 h-9 px-4 rounded mx-4"
      >
        Change description
      </button>
    </div>
    <label class="text-md text-white mb-2 mt-8">Website</label>
    <div class="flex">
      <input
        v-model="website"
        type="text"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        :placeholder="
          repository.website ? repository.website : 'Enter a website...'
        "
      />
      <button
        @click="updateWebsite()"
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
      >
        Change website
      </button>
    </div>
    <label class="text-md text-white mb-2 mt-8">Tags</label>
    <div class="flex">
      <input
        id="AddTagBar"
        type="text"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        placeholder="Search"
      />
      <button
        class="border-gray-500 text-gray-500 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid hover:bg-gray-700"
        @click="addTag()"
      >
        Add tag
      </button>
    </div>
    <div class="flex mt-2 pt-2">
      <div
        v-for="tag in tags"
        :key="tag"
        class="relative bg-pink-600 text-white text-xs font-bold py-1 px-3 rounded-xl mr-4"
      >
        {{ tag }}
        <button
          class="absolute bottom-3 right-0 bg-white border-white border-2 border-solid hover:bg-gray-300 text-gray-800 font-bold rounded py--1"
          @click="deleteTag(tag)"
        >
          x
        </button>
      </div>
    </div>
    <div
      class="flex justify-between border-b border-solid- border-gray-500 w-full pb-4 mt-16"
    >
      <h2 class="text-3xl text-white">Manage access</h2>
      <div class="flex">
        <input
          v-model="collaborator"
          type="text"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="'Enter a username...'"
        />
        <button
          @click="addCollaborator()"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Add people
        </button>
      </div>
    </div>
    <div class="border border-solid border-gray-500 rounded-lg w-full mt-8">
      <div
        v-for="(collaborator, index) in collaborators"
        :key="collaborator"
        class="flex justify-between border-solid border-gray-500 text-white text-base py-2 px-4"
        :class="index < collaborators.length - 1 ? 'border-b' : ''"
      >
        <a>{{ collaborator }}</a>
        <a @click="removeCollaborator(collaborator)" class="text-gray-500 hover:text-red-500 cursor-pointer">Remove</a>
      </div>
    </div>
    <div class="border-b border-solid- border-gray-500 w-full pb-4 mt-16">
      <h2 class="text-3xl text-white">Danger Zone</h2>
    </div>
    <div class="border border-solid border-red-500 rounded-lg w-full mt-8">
      <div
        class="flex justify-between py-4 px-4 border-b border-solid border-gray-500"
      >
        <a class="text-white">{{
          `Change visibility (currently ${visibility})`
        }}</a>
        <div class="flex">
          <button
            @click="setPublic()"
            class="bg-green-600 hover:bg-green-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
            :class="visibility === 'public' ? '' : 'opacity-25'"
          >
            Public
          </button>
          <button
            @click="setPrivate()"
            class="bg-red-600 hover:bg-red-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
            :class="visibility === 'private' ? '' : 'opacity-25'"
          >
            Private
          </button>
        </div>
      </div>
      <div class="flex justify-between py-4 px-4">
        <a class="text-white">Delete repository</a>
        <button
          class="border-red-600 hover:border-red-700 text-red-500 text-sm font-bold py-1 px-4 rounded mx-4 border border-solid"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import {
  fetchRepositoryByUsernameAndName,
  updateRepository,
} from "@/api/repositoryApi";
export default {
  data() {
    return {
      repository: null,
      description: "",
      website: "",
      visibility: "",
      collaborator: "",
      collaborators: [],
      tags: [],
    };
  },
  async created() {
    this.repository = await fetchRepositoryByUsernameAndName(
      this.$route.params.username,
      this.$route.params.repository
    );
    this.tags = this.repository.tags;
    this.collaborators = this.repository.collaborators.map((collaborator) => {
      return collaborator.username;
    });
    this.visibility = this.repository.visibility;
  },
  methods: {
    async addTag() {
      const addTagBar = document.getElementById("AddTagBar");
      if (addTagBar.value !== "") {
        this.tags.push(addTagBar.value);
        addTagBar.value = "";
        await this.updateTags();
      }
    },
    async deleteTag(tag) {
      const myIndex = this.tags.indexOf(tag);
      if (myIndex !== -1) {
        this.tags.splice(myIndex, 1);
        await this.updateTags();
      }
    },
    async updateDescription() {
      await updateRepository(this.repository.id, {
        description: this.repository.description
          ? this.description
          : this.description
          ? this.description
          : null,
      });
      await this.updateData();
    },
    async updateWebsite() {
      await updateRepository(this.repository.id, {
        website: this.repository.website
          ? this.website
          : this.website
          ? this.website
          : null,
      });
      await this.updateData();
    },
    async updateTags() {
      await updateRepository(this.repository.id, {
        tags: this.tags,
      });
      await this.updateData();
    },
    async updateData() {
      this.repository = await fetchRepositoryByUsernameAndName(
        this.$route.params.username,
        this.$route.params.repository
      );
      this.tags = this.repository.tags;
      this.collaborators = this.repository.collaborators.map((collaborator) => {
        return collaborator.username;
      });
      this.visibility = this.repository.visibility;
      this.description = "";
      this.website = "";
    },
    async addCollaborator() {
      if (this.collaborator !== "") {
        await updateRepository(this.repository.id, {
          collaborators: this.collaborators.concat(this.collaborator),
        });
        await this.updateData();
        this.collaborator = "";
      }
    },
    async removeCollaborator(value) {
      await updateRepository(this.repository.id, {
        collaborators: this.collaborators.filter(
          (collaborator) => collaborator !== value
        ),
      });
      await this.updateData();
    },
    async setPublic() {
      this.visibility = "public";
      await updateRepository(this.repository.id, {
        visibility: this.visibility,
      });
    },
    async setPrivate() {
      this.visibility = "private";
      await updateRepository(this.repository.id, {
        visibility: this.visibility,
      });
    },
  },
};
</script>
