<template>
  <div class="flex flex-col w-full px-48 mt-16">
    <div class="border-b border-solid- border-gray-500 w-full pb-4">
      <h2 class="text-3xl text-white">General</h2>
    </div>
    <label class="text-md text-white mb-2 mt-8">Repository name</label>
    <div class="flex">
      <input
        type="text"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        placeholder="Hello"
      />
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
      >
        Rename
      </button>
    </div>
    <label class="text-md text-white mt-8 mb-2">Description</label>
    <div class="flex items-end">
      <textarea
        type="text"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        placeholder="This is the repository description it can be quite long and have multiple lines"
      />
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 h-9 px-4 rounded mx-4"
      >
        Change description
      </button>
    </div>
    <label class="text-md text-white mb-2 mt-8">Website</label>
    <div class="flex">
      <input
        type="text"
        class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        placeholder="Website url"
      />
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
      >
        Change website
      </button>
    </div>
    <div
      class="flex justify-between border-b border-solid- border-gray-500 w-full pb-4 mt-16"
    >
      <h2 class="text-3xl text-white">Manage access</h2>
      <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
      >
        Add people
      </button>
    </div>
    <div class="border border-solid border-gray-500 rounded-lg w-full mt-8">
      <div
        v-for="(collaborator, index) in collaborators"
        :key="collaborator.name"
        class="flex justify-between border-solid border-gray-500 text-white text-base py-2 px-4"
        :class="index < collaborators.length - 1 ? 'border-b' : ''"
      >
        <a>{{ collaborator.name }}</a>
        <a class="text-gray-500 hover:text-red-500 cursor-pointer">Remove</a>
      </div>
    </div>
    <div class="border-b border-solid- border-gray-500 w-full pb-4 mt-16">
      <h2 class="text-3xl text-white">Danger Zone</h2>
    </div>
    <div class="border border-solid border-red-500 rounded-lg w-full mt-8">
      <div class="flex justify-between py-4 px-4 border-b border-solid border-gray-500">
        <a class="text-white">Change visibility (currently private)</a>
        <div class="flex">
          <button
            class="bg-green-600 hover:bg-green-700 opacity-25 text-white text-sm font-bold py-1 px-4 rounded mx-4"
          >
            Public
          </button>
          <button
            class="bg-red-600 hover:bg-red-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
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
export default {
  data() {
    return {
      collaborators: [{ name: "user1" }, { name: "user2" }, { name: "user3" }],
    };
  },
};
</script>
