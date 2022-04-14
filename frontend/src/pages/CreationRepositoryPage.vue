<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex flex-col w-full px-48 mt-16">
      <div class="border-b border-solid- border-gray-500 w-full pb-4">
        <h2 class="text-3xl text-white">Create a new repository</h2>
      </div>
      <label class="text-md text-white mb-2 mt-8">Repository name</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        />
      </div>
      <label class="text-md text-white mt-8 mb-2">Description</label>
      <div class="flex items-end">
      <textarea
          type="text"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
      />
      </div>
      <label class="text-md text-white mb-2 mt-8">Website</label>
      <div class="flex">
        <input
            type="text"
            class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
        />
      </div>

      <label class="text-md text-white mb-2 mt-8">Visibility</label>
      <div>
        <button
            v-if="visibility==='Private'"
            class="border-gray-500 text-gray-500 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid inline-block mr-auto my-2 ml-4 hover:bg-gray-700"
            @click="setPublic()"
        >
          Public
        </button>
        <button
            v-if="visibility==='Private'"
            class="border-pink-600 text-pink-600 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid inline-block mr-auto my-2 ml-4 hover:bg-gray-700"
            @click="setPrivate()"
        >
          Private
        </button>
        <button
            v-if="visibility==='Public'"
            class="border-pink-600 text-pink-600 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid inline-block mr-auto my-2 ml-4 hover:bg-gray-700"
            @click="setPublic()"
        >
          Public
        </button>
        <button
            v-if="visibility==='Public'"
            class="border-gray-500 text-gray-500 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid inline-block mr-auto my-2 ml-4 hover:bg-gray-700"
            @click="setPrivate()"
        >
          Private
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
        <button class="border-gray-500 text-gray-500 text-xs font-bold py-1 px-1 rounded-xl border-2 border-solid hover:bg-gray-700"
                @click="addTag()">
          Add tag
        </button>
      </div>
      <div class="flex mt-2 pt-2">
        <div v-for="tag in tags" :key="tag" class="relative bg-pink-600 text-white text-xs font-bold py-1 px-3 rounded-xl mr-4" >
          {{ tag }}
          <button class="absolute bottom-3 right-0 bg-white border-whitex border-2 border-solid hover:bg-gray-300 text-gray-800 font-bold rounded py--1"
          @click="deleteTag(tag)"
          >x</button>
        </div>
      </div>
      <div
          class="flex justify-between border-b border-solid- border-gray-500 w-full pb-4 mt-16"
      >
        <h2 class="text-3xl text-white">Manage access</h2>
        <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4 "
        >
          Add people
        </button>
      </div>
      <div class="border border-solid border-gray-500 rounded-lg w-full mt-8" v-if="collaborators.length>0">
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
      <div class=" border-solid border-gray-500 w-full mt-8" v-if="collaborators.length===0">
        <a class="text-base text-gray-500 ">There is no collaborator</a>
      </div>
      <div
          class=" justify-between border-solid- border-gray-500 w-full pb-4 mt-16"
      >
        <button
            class="bg-pink-600 border-pink-600 border-2 border-solid hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded "
            @click="confirm()"
        >
          Confirm
        </button>
        <button
            class="border-gray-500 hover:bg-gray-700 text-gray-500 text-sm font-bold py-1 px-4 rounded border-2 border-solid inline-block mr-auto my-1 ml-4"
            @click="cancel()"
        >
          Cancel
        </button>
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
