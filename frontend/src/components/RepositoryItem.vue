<template>
    <div class="flex flex-col border-b pb-4 mt-4">
        <div class="flex items-center">
            <h2 class="text-white font-bold text-3xl mr-4">GLO-2005</h2>
            <div class="border-pink-600 text-pink-600 text-sm font-bold py-1 px-2 border-2 border-solid rounded-xl">Private</div>
        </div>
        <p class="text-white text-base text-justify">This is the description of the repository.</p>
        <div class="flex mt-2">
            <div v-for="tag in tags" :key="tag" class="bg-pink-600 text-white text-xs font-bold py-1 px-2 rounded-xl mr-4">
                {{ tag }}
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            tags: ["Java", "Python", "MySQL"]
        };
    },
}
</script>