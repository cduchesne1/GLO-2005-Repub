<template>
    <div :class="`bg-pink-600 rounded-full flex justify-center items-center w-${size} h-${size}`" @click="action">
        <h3 class="text-lg text-white font-bold text-center">{{ name.charAt(0).toUpperCase() }}</h3>
    </div>
</template>
<script>
export default {
    props: {
        size: {
            type: Number,
            default: 10,
        },
        name: {
            type: String,
            required: true,
        },
        action: {
            type: Function,
            required: true,
        },
    },
}
</script>