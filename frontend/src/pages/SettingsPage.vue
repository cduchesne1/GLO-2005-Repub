<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex flex-col w-full px-48 mt-16">
      <div class="border-b border-solid- border-gray-500 w-full pb-4">
        <h2 class="text-3xl text-white">Settings</h2>
      </div>
      <label class="text-md text-white mb-2 mt-8">Name</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
            placeholder="Hello"
        />
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change name
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">Email</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
            placeholder="Hello"
        />
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change email
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">UserName</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
            placeholder="Hello"
        />
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change UserName
        </button>
      </div>
      <label class="text-md text-white mt-8 mb-2">Bio</label>
      <div class="flex items-end">
      <textarea
          type="text"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          placeholder="This is the repository description it can be quite long and have multiple lines"
      />
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 h-9 px-4 rounded mx-4"
        >
          Change bio
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
      <label class="text-md text-white mb-2 mt-8">Company Name</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
            placeholder="Website url"
        />
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change name
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">Location</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
            placeholder="Website url"
        />
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change location
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
        <div class="flex justify-between py-4 px-4">
          <a class="text-white">Delete account</a>
          <button
              class="border-red-600 hover:border-red-700 text-red-500 text-sm font-bold py-1 px-4 rounded mx-4 border border-solid"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
  },
  data() {
    return {
      collaborators: [],
      visibility: 'Public',
      tags: [],
    };
  },
  methods:{
    setPublic(){
      this.visibility='Public';
    },
    setPrivate(){
      this.visibility='Private';
    },
    addTag(){
      const addTagBar = document.getElementById("AddTagBar");
      if(addTagBar.value !== ""){
        this.tags.push(addTagBar.value);
        addTagBar.value="";
      }
    },
    deleteTag(tag){
      const myIndex = this.tags.indexOf(tag);
      if (myIndex !== -1) {
        this.tags.splice(myIndex, 1);
      }
    },
    confirm(){

    },
    cancel(){
      this.$router.back();
    }
  }
};
</script>
