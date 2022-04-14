<template>
  <div>
    <div
      class="flex items-stretch justify-between overflow-hidden whitespace-nowrap overflow-x-auto text-lg text-white"
    >
      <ul class="flex">
        <li
          v-for="tab in tabs"
          :key="tab.name"
          class="flex items-center justify-center border-b border-solid border-gray-500 px-8 cursor-pointer"
          :class="tab.isActive ? 'border-pink-600 font-bold cursor-default' : ''"
        >
          <a :href="tab.href" @click="selectTab(tab)">
            {{ tab.name }}
          </a>
        </li>
      </ul>
    </div>
    <div>
      <slot></slot>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tabs: [],
    };
  },
  created() {
    this.tabs = this.$children;
  },
  methods: {
    selectTab(selectedTab) {
      this.tabs.forEach((tab) => {
        tab.isActive = tab.name == selectedTab.name;
      });
    },
  },
};
</script>
