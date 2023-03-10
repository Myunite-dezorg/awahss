<script>
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";

const CODES_QUERY = gql`
    query {
      getMsgcodes {
        id
        description
        code
        type
      }
    }
  `;

export default {
  name: "MsgCodesComp",
  setup() {
    const { result, loading, error } = useQuery(CODES_QUERY);
    return {
      result,
      loading,
      error,
    };
  },
  data() {
    return {
      // Initialize your apollo data
      getMsgcodes: "",
    };
  },
  apollo: {
    // Simple query that will update the 'hello' vue property
    getMsgcodes: CODES_QUERY,
  },
};
</script>

<template>
  <div class="overflow-x-auto">
    <div
      class="pt-4 mb-3 text-center text-lg transition-all duration-200 md:text-xl"
    >
      <span class="text-accent">M<span class="uppercase text-light">essages </span></span>
      <span class="text-base-content text-bold">C<span class="uppercase text-bold">odes</span></span>
    </div>
    <table class="table w-full">
      <!-- head -->
      <thead>
        <tr>
          <th>Code</th>
          <th>Description</th>
        </tr>
      </thead>
      <p v-if="error" class="text-center font-light text-slate-500">
        Something went wrong...
      </p>
      <p v-if="loading" class="text-center font-light text-pink-500">
        <button type="button" class="... bg-indigo-500" disabled>
          <svg class="... mr-3 h-5 w-5 animate-spin" viewBox="0 0 24 24">
            https://icons8.com/icon/J18pPgWKQBRT/spinning-circle
          </svg>
          Processing...
        </button>
      </p>
      <tbody v-for="i in result.getMsgcodes" v-else :key="i.id">
        <!-- row 1 -->
        <tr class="hover">
          <th>{{ i.code }}</th>
          <td>{{ i.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
