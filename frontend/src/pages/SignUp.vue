<template>
  <div
    class="bg-gray-800 w-full h-full flex flex-col min-h-screen items-center justify-center"
  >
    <img class="w-24" src="../assets/rePubIcon.svg" />
    <h1 class="text-3xl text-white font-bold max-w-xl mt-8">
      Create an account on RePub
    </h1>
    <div
      class="flex flex-col bg-white bg-opacity-10 border-2 border-gray-300 rounded-xl p-8 mt-8"
    >
      <form @submit.prevent="signUp" class="flex flex-col">
        <label for="email" class="text-md text-white mb-2">Email</label>
        <input
          name="email"
          type="email"
          v-model="email"
          class="bg-gray-800 text-white w-96 py-2 px-2 rounded-lg"
        />
        <a v-if="emailError" class="text-md text-red-600 mb-2">{{
          emailError
        }}</a>
        <label for="username" class="text-md text-white mt-8 mb-2"
          >Username</label
        >
        <input
          name="username"
          type="text"
          v-model="username"
          class="bg-gray-800 text-white w-96 py-2 px-2 rounded-lg"
        />
        <a v-if="usernameError" class="text-md text-red-600 mb-2">{{
          usernameError
        }}</a>
        <label for="name" class="text-md text-white mt-8 mb-2">Full Name</label>
        <input
          name="name"
          type="text"
          v-model="name"
          class="bg-gray-800 text-white w-96 py-2 px-2 rounded-lg"
        />
        <a v-if="nameError" class="text-md text-red-600 mb-2">{{
          nameError
        }}</a>
        <label for="password" class="text-md text-white mt-8 mb-2"
          >Password</label
        >
        <input
          name="password"
          type="password"
          v-model="password"
          class="bg-gray-800 text-white w-96 py-2 px-2 rounded-lg"
        />
        <a v-if="passwordError" class="text-md text-red-600 mb-2">{{
          passwordError
        }}</a>
        <button
          class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded mt-8"
          type="submit"
        >
          Sign Up
        </button>
      </form>
    </div>
    <div
      class="flex bg-white bg-opacity-10 border-2 border-gray-300 rounded-xl p-4 mt-8"
    >
      <a class="text-md text-white mr-2">Already have an account?</a>
      <a class="text-md text-pink-600">Sign In</a>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      email: "",
      name: "",
      username: "",
      password: "",
      emailError: null,
      nameError: null,
      usernameError: null,
      passwordError: null,
    };
  },
  methods: {
    async signUp() {
      if (this.checkForm()) {
        const user = {
          email: this.email,
          name: this.name,
          username: this.username,
          password: this.password,
        };
        const response = await fetch(`${process.env.VUE_APP_API_URL}/signup`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(user),
        });

        if (response.status === 200) {
          this.$router.push("/profile");
        } else {
          if (response.body.data.desc === "Email already exists") {
            this.emailError = "Email already exists";
          } else if (response.body.data.desc === "Username already exists") {
            this.usernameError = "Username already exists";
          }
        }
      }
    },
    checkForm() {
      this.emailError = null;
      this.nameError = null;
      this.usernameError = null;
      this.passwordError = null;
      if (this.email === "") {
        this.emailError = "Email is required";
      } else if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email) === false) {
        this.emailError = "Email is invalid";
      }

      if (this.name === "") {
        this.nameError = "Name is required";
      }
      if (this.username === "") {
        this.usernameError = "Username is required";
      }
      if (this.password === "") {
        this.passwordError = "Password is required";
      }

      if (
        this.emailError ||
        this.nameError ||
        this.usernameError ||
        this.passwordError
      ) {
        return false;
      }
      return true;
    },
  },
};
</script>
