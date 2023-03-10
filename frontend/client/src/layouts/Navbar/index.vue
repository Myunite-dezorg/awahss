<!-- eslint-disable vue/no-export-in-script-setup -->
<script setup lang="ts">
import { defineComponent } from "vue";
import ThemeChange from "./components/ThemeChange/index.vue";
import LocalesChange from "./components/LocalesChange/index.vue";
import Clock from "./components/ClockBar/index.vue";
</script>

<template>
  <div
    class="text-base-content sticky top-0 z-30 flex h-16 w-full justify-center opacity-90 backdrop-blur transition-all duration-100"
  >
    <nav class="navbar w-full">
      <div class="flex flex-1 md:gap-1 lg:gap-2">
        <RouterLink
          to="/"
          aria-current="page"
          aria-label="Homepage"
          class="btn-ghost btn px-2"
        >
          <div
            class="text-primary inline-flex text-lg transition-all duration-200 md:text-3xl"
          >
            <span class="text-accent">V<span class="lowercase">ite</span></span>
            <span class="text-base-content"
              >B<span class="lowercase">oot</span></span
            >
          </div>
        </RouterLink>
        <div class="container mx-auto mt-4">
          <Clock />
        </div>
      </div>
      <div>
        
        <ThemeChange />
        <LocalesChange />
        <span
          class="tooltip tooltip-bottom before:text-xs before:content-[attr(data-tip)]"
          data-tip="GitHub"
        >
          <span class="flex-none items-center">
            <a
              aria-label="Github"
              target="_blank"
              href="https://github.com/kirklin/vite-boot"
              class="btn-ghost drawer-button btn-square btn normal-case"
            >
              <IMdiGithub />
            </a>
          </span>
        </span>
      </div>
    </nav>
  </div>
</template>
