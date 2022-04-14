<template>
  <div class="flex flex-col">
    <div class="flex flex-col">
      <div class="flex justify-between w-full">
        <div class="flex items-center">
          <h2 class="text-4xl text-white mr-4">
            This is the title of the task
          </h2>
          <h2 class="text-4xl text-gray-500">#32</h2>
        </div>
        <div class="flex items-center">
            <button
            class="bg-gray-500 hover:bg-gray-600 text-white text-sm font-bold py-1 px-4 rounded mx-4 h-8"
          >
            Edit
          </button>
          <button
            class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-1 px-4 rounded h-8 w-24"
          >
            New task
          </button>
        </div>
      </div>
      <div class="flex items-center">
          <div class="bg-green-500 rounded-full py-2 px-4 text-white w-16 flex justify-center">Open</div>
          <a class="text-white text-base font-bold">johndoe1</a>
          <a></a>
      </div>
    </div>
  </div>
</template>
