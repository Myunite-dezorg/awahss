<script lang="ts">
import { computed, defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const currentTime = ref(new Date());
    const isUtc = ref(false);

    setInterval(() => {
      currentTime.value = new Date();
    }, 1000);

    const displayTime = computed(() => {
      const time = isUtc.value
        ? currentTime.value.getUTCHours()
        : currentTime.value.getHours();
      const paddedTime = time.toString().padStart(2, "0");
      return `${paddedTime}:${currentTime.value
        .getMinutes()
        .toString()
        .padStart(2, "0")}:${currentTime.value
        .getSeconds()
        .toString()
        .padStart(2, "0")}`;
    });

    const toggleUtc = () => {
      isUtc.value = !isUtc.value;
    };

    return {
      currentTime,
      isUtc,
      displayTime,
      toggleUtc,
    };
  },
});
</script>

<template>
  <div class="flex items-center space-x-2">
    <div class="font-mono text-base font-bold text-neutral-200">
      {{ displayTime }}
    </div>
    <div>
      <button class="btn btn-ghost" aria-pressed="true" @click="toggleUtc">
        {{ isUtc ? "Local Time" : "UTC" }}
      </button>
    </div>
  </div>
</template>
