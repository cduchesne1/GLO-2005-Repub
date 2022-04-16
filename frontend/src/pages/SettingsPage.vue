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
          v-model="name"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="user.name"
        />
        <button
          @click="updateUserProfile()"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change name
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">Email</label>
      <div class="flex">
        <input
          type="email"
          v-model="email"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="user.email"
        />
        <button
          @click="updateUserProfile()"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change email
        </button>
      </div>
      <a v-if="emailError" class="text-md text-red-600 mb-2">{{
        emailError
      }}</a>
      <label class="text-md text-white mb-2 mt-8">Username</label>
      <div class="flex">
        <input
          type="text"
          v-model="username"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="user.username"
        />
        <button
          @click="updateUserProfile()"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change username
        </button>
      </div>
      <label class="text-md text-white mt-8 mb-2">Bio</label>
      <div class="flex items-end">
        <textarea
          type="text"
          v-model="bio"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="user.bio ? user.bio : 'Tell us about yourself...'"
        />
        <button
          @click="updateUserProfile('bio')"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 h-9 px-4 rounded mx-4"
        >
          Change bio
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">Website</label>
      <div class="flex">
        <input
          type="text"
          v-model="website"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="user.website ? user.website : 'Link to your website...'"
        />
        <button
          @click="updateUserProfile('website')"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change website
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">Company Name</label>
      <div class="flex">
        <input
          type="text"
          v-model="company"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="
            user.company ? user.company : 'What company do you work for...'
          "
        />
        <button
          @click="updateUserProfile('company')"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change company
        </button>
      </div>
      <label class="text-md text-white mb-2 mt-8">Location</label>
      <div class="flex">
        <input
          type="text"
          v-model="location"
          class="bg-gray-900 text-white w-96 py-2 px-2 rounded-lg"
          :placeholder="
            user.location ? user.location : 'Where are you located...'
          "
        />
        <button
          @click="updateUserProfile('location')"
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded mx-4"
        >
          Change location
        </button>
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
import { updateUserProfile, fetchUser } from "@/api/userApi";

export default {
  components: {
    LoggedTopBar,
    FooterComponent,
  },
  data() {
    return {
      user: null,
      name: "",
      email: "",
      username: "",
      bio: "",
      website: "",
      company: "",
      location: "",
      emailError: null,
    };
  },
  async created() {
    this.user = await fetchUser(this.$store.user.id);
  },
  methods: {
    async updateUserProfile(source) {
      this.emailError = null;
      if (
        this.email &&
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email) === false
      ) {
        this.emailError = "Please enter a valid email address";
        return;
      }
      const data = {
        name: this.name ? this.name : null,
        email: this.email ? this.email : null,
        username: this.username ? this.username : null,
        bio:
          this.user.bio && source === "bio"
            ? this.bio
            : this.bio
            ? this.bio
            : null,
        website:
          this.user.website && source === "website"
            ? this.website
            : this.website
            ? this.website
            : null,
        company:
          this.user.company && source === "company"
            ? this.company
            : this.company
            ? this.company
            : null,
        location:
          this.user.location && source === "location"
            ? this.location
            : this.location
            ? this.location
            : null,
      };
      await updateUserProfile(this.$store.user.id, data);
      this.user = await fetchUser(this.$store.user.id);
      this.updateStore();
      this.resetFields();
    },
    updateStore() {
      this.$actions.setName(this.user.name);
      this.$actions.setUsername(this.user.username);
      this.$actions.setEmail(this.user.email);
    },
    resetFields() {
      this.name = "";
      this.email = "";
      this.username = "";
      this.bio = "";
      this.website = "";
      this.company = "";
      this.location = "";
    },
  },
};
</script>
