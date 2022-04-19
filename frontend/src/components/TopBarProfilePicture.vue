<template>
    <div class="flex">
        <div :class="` bg-pink-600 rounded-full flex justify-center items-center w-${size} h-${size}`" @click="action">
            <h3 class="text-lg text-white font-bold text-center" :class="size > 24 ? 'text-8xl' : ''">{{ name.charAt(0).toUpperCase() }}</h3>
        </div>
        <div
            class="shadow-xl pl-4"
            :class="isOpen ? 'flex' : 'hidden'"
        >
            <div
                class="bg-gray-900 border-2 rounded-xl border-black p-2 align-baseline"
                :class="isConnected ? 'flex' : 'hidden'"
            >
                <button
                    class="px-1.5 bg-transparent text-gray-300 mb-1 hover:text-pink-600"
                    v-on:click="goToPath"
                >
                    Your account
                </button>
                <button
                    class="px-1.5 bg-transparent text-gray-300 hover:text-pink-600"
                    v-on:click="logout"
                >
                    Sign out
                </button>
            </div>
        </div>
    </div>
</template>
<script>
import { logout } from "@/api/authApi"
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
        path: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            isConnected: undefined,
            isOpen: false,
        }
    },
    created() {
        this.isConnected = this.$store.isConnected;
    },
    watch: {
        $store: {
            handle() {
                this.isConnected = this.$store.isConnected;
            },
            deep: true,
        }
    },
    methods: {
        action() {
            this.isOpen = !this.isOpen;
        },
        goToPath() {
            this.$router.push(this.path);
        },
        async logout() {
            await logout()
            this.$actions.disconnect();
            this.$actions.setName("");
            this.$actions.setEmail("");
            this.$actions.setUsername("");
            this.$router.push({ path: "/login" });
        },
    },
}
</script>