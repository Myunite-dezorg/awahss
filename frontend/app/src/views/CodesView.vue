<template lang="">
  <div
    class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl"
  >
    <div class="md:flex">
      <div class="p-8">
        <div
          class="uppercase text-center tracking-wide text-sm  text-pink-700 font-semibold"
        >
          iBase data
        </div>
        <a
          class="block mt-1 text-sm text-center font-light text-slate-400"
          >Messages code types</a
        >
        <Codes />
      </div>
    </div>
  </div>
</template>
<script>
import Codes from "@/components/apps/ibase/codes/MsgCodes.vue";
export default {
  components: {
    Codes,
  },
};
</script>
<style lang=""></style>
