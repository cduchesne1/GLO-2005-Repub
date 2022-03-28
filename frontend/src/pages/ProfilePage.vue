<template>
  <div class="bg-gray-800 w-full h-full flex flex-col min-h-screen">
    <LoggedTopBar />
    <div class="flex px-24 justify-between items-center">
      <div class="flex">
        <img src="../assets/bigProfilePic.svg" />
        <div class="flex flex-col justify-center ml-4">
          <h1 class="text-5xl text-white font-bold">John Doe</h1>
          <h2 class="text-pink-600 font-bold text-2xl">johndoe1</h2>
          <div class="flex mt-4">
            <div class="flex items-center mr-4">
              <img class="w-7" src="../assets/companyIcon.svg" />
              <a class="text-sm text-white">Microsoft</a>
            </div>
            <div class="flex items-center mr-4">
              <img class="w-7" src="../assets/locationIcon.svg" />
              <a class="text-sm text-white">Canada</a>
            </div>
            <div class="flex items-center mr-4">
              <img class="w-6 mr-2" src="../assets/websiteIcon.svg" />
              <a class="text-sm text-white" href="https://www.google.com"
                >https://www.google.com/</a
              >
            </div>
          </div>
          <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded mx-4 mt-4"
          >
            Edit Profile
          </button>
        </div>
      </div>
      <div>
        <h3 class="text-white font-bold text-lg">A little about me:</h3>
        <p class="text-white text-base max-w-sm text-justify">This is the description of the user. He is a passionate person and likes to code.</p>
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
};
</script>
