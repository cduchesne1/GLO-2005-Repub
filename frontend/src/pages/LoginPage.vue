<template>
    <div class="bg-gray-800 w-full h-full flex flex-col min-h-screen items-center justify-center">
        <img class="w-24" src="../assets/rePubIcon.svg" />
        <h1 class="text-3xl text-white font-bold max-w-xl mt-8">Sign in to RePub</h1>
        <div class="flex flex-col bg-white bg-opacity-10 border-2 border-gray-300 rounded-xl p-8 mt-8">
            <label class="text-md text-white mb-2">Email address</label>
            <input type="text" v-model="email" class="bg-gray-800 text-white w-96 py-2 px-2 rounded-lg"/>
            <label class="text-md text-white mt-8 mb-2">Password</label>
            <input type="password" v-model="password" class="bg-gray-800 text-white w-96 py-2 px-2 rounded-lg"/>
            <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded mt-8"
            @click="sendCredentials"
          >
            Sign In
          </button>
        </div>
        <div v-if="showInvalidCredential"
          class="text-lg text-pink-600 pt-6"
        >
          Invalid password and email combination
        </div>
        <div class="flex bg-white bg-opacity-10 border-2 border-gray-300 rounded-xl p-4 mt-8">
            <div class="text-md text-white mr-2">Don't have an account?</div>
            <div @click="goToSignUp" class="text-md text-pink-600 cursor-pointer">Sign Up</div>
        </div>
    </div>
</template>


<script>
import authApi from "../api/AuthApi"
export default {
  data() {
    return {
      email: this.email,
      password: this.password,
      showInvalidCredential: false
    }
  },
  methods: {
    sendCredentials: async function() {
      const data = await authApi.login(this.email, this.password)
        if (data) {
          this.$actions.connect();
          this.$actions.setName(data.name);
          this.$actions.setEmail(this.email);
          this.$actions.setUsername(data.username);
          this.$actions.setId(data.id);
          this.$router.push({ path: "/logged" });
        } else {
          this.showInvalidCredential = true
        }
    },
    goToSignUp: async function () {
      if (this.$store.isConnected){
        this.$router.push("/logged");
      } else {
        this.$router.push({ path: "/signup/" });
      }
      
    },
  }
}
</script>
