<template>
  <div
    class="bg-gray-800 w-full h-full flex flex-col min-h-screen justify-between"
  >
    <HomeTopBar />
    <div class="flex justify-center items-center px-14">
      <div class="mr-16">
        <h1 class="text-5xl text-white font-bold max-w-xl">
          The best tool for the good developers!
        </h1>
        <p class="text-base text-white max-w-xl mt-4">
          GitGud is the system by excellence for collaborating on software
          projects. It makes the development easier for everyone and helps
          create quality projects.
        </p>
      </div>
      <img src="../assets/planet.svg" />
    </div>
    <FooterComponent />
  </div>
</template>
<script>
import HomeTopBar from "@/components/HomeTopBar";
import FooterComponent from "@/components/FooterComponent";
export default {
  components: {
    HomeTopBar,
    FooterComponent,
  },
};
</script>
