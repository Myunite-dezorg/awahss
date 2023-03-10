<template>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>|
    <router-link to="/codes">Codes</router-link> -->
    <NavBar />

  <router-view/>
</template>
<script>
import NavBar from "./components/ui/NavBar.vue"

export default {
  components: {
    NavBar
  }
}
</script>

