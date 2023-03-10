import { useLocalStorage } from "@vueuse/core";
import { createApp } from "vue";

//Apollo
import { provide, h } from "vue";
import { DefaultApolloClient } from "@vue/apollo-composable";
import { ApolloClient, InMemoryCache } from "@apollo/client/core";
// Vue Router
import { createPinia } from "pinia";
import { createI18n } from "vue-i18n";

import { router } from "./router";

import { registerStore } from "./store";
import App from "~/App.vue";

import "@kirklin/reset-css/kirklin.css";
import "~/styles/tailwind.css";
import "~/styles/main.css";


const cache = new InMemoryCache();

const apolloClient = new ApolloClient({
  cache,
  uri: "http://127.0.0.1:8000/graphql",
});

// const app = createApp(App);
const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },

  render: () => h(App),
});
const messages = Object.fromEntries(
  Object.entries(
    import.meta.glob<{ default: any }>("./locales/*.json", { eager: true }))
    .map(([key, value]) => {
      return [key.slice(10, -5), value.default];
    }),
);
app.use(createI18n({
  legacy: false,
  locale: unref(useLocalStorage("locale", "zh-CN")),
  messages,
}));
app.use(createPinia());
registerStore();
app.use(router);
app.mount("#app");
