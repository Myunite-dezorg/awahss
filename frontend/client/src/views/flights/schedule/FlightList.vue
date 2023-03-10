<script lang="ts">
import { computed, defineComponent } from "vue";
import { Flight } from "@/models/flight";
import { useStore } from "@/store";

export default defineComponent({
  name: "Home",
  setup() {
    const store = useStore();
    const flights = computed(() => store.state.flights);

    return {
      flights,
    };
  },
});
</script>

<template>
  <div>
    <h1>Flight Schedule App</h1>
    <ul>
      <li v-for="flight in flights" :key="flight.id">
        {{ flight.airline }} - {{ flight.origin }} to {{ flight.destination }}
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>
