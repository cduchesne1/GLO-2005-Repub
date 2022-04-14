<template>
  <div v-show="isActive" />
</template>
<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    selected: {
      type: Boolean,
      default: false,
    },
    href: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      isActive: false,
    };
  },
  mounted() {
    this.isActive = this.selected;
  },
};
</script>
