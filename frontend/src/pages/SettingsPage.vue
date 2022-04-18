<template>
  <div class="bg-gray-800 w-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex flex-col w-full px-48 mt-16">
      <div class="border-b border-solid- border-gray-500 w-full pb-4">
        <h2 class="text-3xl text-white">Settings</h2>
      </div>
      <div class="text-center mt-8" v-if="isLoading">
        <svg class="inline mr-3 w-8 h-8 text-pink-600 animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
          <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
        </svg>
      </div>
      <div class="flex flex-col w-full " v-if="!isLoading">
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
          @click="deleteAccount()"
            class="border-red-600 hover:border-red-700 text-red-500 text-sm font-bold py-1 px-4 rounded mx-4 border border-solid"
          >
            Delete
          </button>
        </div>
      </div>
      </div>
    </div>
    <FooterComponent v-if="!isLoading"/>
  </div>
</template>
<script>
import LoggedTopBar from "@/components/LoggedTopBar";
import FooterComponent from "@/components/FooterComponent";
import { updateUserProfile, fetchUser, deleteUser } from "@/api/userApi";
import authApi from "../api/AuthApi"

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
      isLoading: false,
    };
  },
  async created() {
    this.isLoading = true;
    this.user = await fetchUser(this.$store.user.id);
    this.isLoading = false;
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
    async deleteAccount() {
      if (confirm("Are you sure you want to delete your account?")) {
        await deleteUser(this.$store.user.id);
        await authApi.logout();
        this.$actions.setName("");
        this.$actions.setUsername("");
        this.$actions.setEmail("");
        this.$actions.setId(null);
        this.$actions.disconnect();
        this.$router.push("/");
      }
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
