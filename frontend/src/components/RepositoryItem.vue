<template>
    <div class="flex flex-col border-b pb-4 mt-4">
        <div class="flex items-center">
            <h2 @click="goToRepository()" class="text-white font-bold text-3xl mr-4 cursor-pointer hover:text-pink-600">{{ repository.name }}</h2>
            <div class="border-pink-600 text-pink-600 text-sm font-bold py-1 px-2 border-2 border-solid rounded-xl">{{ visibility }}</div>
        </div>
        <p class="text-white text-base text-justify">{{ repository.description }}</p>
        <div class="flex mt-2">
            <div v-for="tag in repository.tags" :key="tag" class="bg-pink-600 text-white text-xs font-bold py-1 px-2 rounded-xl mr-4">
                {{ tag }}
            </div>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        repository: {
            required: true,
        },
    },
    computed: {
        visibility() {
            const visibility = this.repository.visibility;
            return visibility === 'public' ? 'Public' : 'Private';
        },
    },
    methods: {
        goToRepository() {
            this.$router.push(`/${this.repository.owner.username}/${this.repository.name}`);
        },
    },
}
</script>