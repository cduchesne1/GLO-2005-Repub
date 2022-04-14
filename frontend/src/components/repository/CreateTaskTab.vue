<template>
  <div
    class="flex flex-col border border-solid border-gray-500 rounded-lg px-4 py-4 mx-48 mt-16"
  >
    <input
      type="text"
      class="bg-gray-900 text-white py-2 px-2 rounded-lg"
      placeholder="Title"
    />
    <textarea
      type="text"
      class="bg-gray-900 text-white h-48 py-2 px-2 rounded-lg mt-8"
      placeholder="Leave a comment"
    />
    <div class="flex justify-end mt-4">
        <button
        class="bg-pink-600 hover:bg-pink-700 text-white text-sm font-bold py-2 px-8 rounded"
      >
        Submit new task
      </button>
    </div>
  </div>
</template>
