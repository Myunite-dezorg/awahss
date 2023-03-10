<template>
  <nav
    class="relative flex flex-wrap items-center justify-between px-2 py-3 bg-slate-800 mb-3"
  >
    <div
      class="container px-4 mx-auto flex flex-wrap items-center justify-between"
    >
      <div
        class="w-full relative flex justify-between lg:w-auto px-4 lg:static lg:block lg:justify-start"
      >
        <a
          class="text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white"
          href="#pablo"
        >
          AWAHSS 
        </a>
        <button
          class="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
          type="button"
          v-on:click="toggleNavBar()"
        >
          <i class="fas fa-bars"></i>
        </button>
      </div>
      <div
        v-bind:class="{ hidden: !showMenu, flex: showMenu }"
        class="lg:flex lg:flex-grow items-center"
      >
        <ul class="flex flex-col lg:flex-row list-none ml-auto">
          <li class="nav-item">
            <router-link to="/" class="px-3 py-2 flex items-center text-xs uppercase font-normal leading-snug text-white hover:opacity-75">
              <i class="fab fa-facebook-square text-lg leading-lg text-white opacity-75"
              /><span class="ml-2">Home</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="px-3 py-2 flex items-center text-xs uppercase font-normal leading-snug text-white hover:opacity-75">
              <i class="fab fa-facebook-square text-lg leading-lg text-white opacity-75"
              /><span class="ml-2">About</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/codes" class="px-3 py-2 flex items-center text-xs uppercase font-normal leading-snug text-white hover:opacity-75">
              <i class="fab fa-facebook-square text-lg leading-lg text-white opacity-75"
              /><span class="ml-2">Messages</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    toggleNavBar: function () {
      this.showMenu = !this.showMenu;
    },
  },
};
</script>
