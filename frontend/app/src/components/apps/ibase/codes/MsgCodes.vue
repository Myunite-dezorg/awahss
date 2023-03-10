<template>
  <div class="flex flex-col">
    <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="inline-block min-w-full py-2 sm:px-6 lg:px-8">
        <div class="overflow-hidden">
          <table class="min-w-full text-left text-sm font-light">
            <thead class="border-b font-medium dark:border-slate-300">
              <tr>
                <th scope="col" class="px-6 py-4 font-light text-slate-700">Code</th>
                <th scope="col" class="px-6 py-4 font-light text-right text-slate-700">Description</th>
              </tr>
            </thead>
            <p class="font-light text-slate-500 text-center" v-if="error">Something went wrong...</p>
            <p class="font-light text-pink-500 text-center" v-if="loading">
                <button type="button" class="bg-indigo-500 ..." disabled>
                <svg class="animate-spin h-5 w-5 mr-3 ..." viewBox="0 0 24 24">
                    https://icons8.com/icon/J18pPgWKQBRT/spinning-circle
                </svg>
                Processing...
                </button>
            </p>
            <tbody v-else v-for="i in result.getMsgcodes" :key="i.id">
              <tr
                class="border-b transition duration-300 ease-in-out hover:bg-slate-200 dark:border-slate-200 dark:hover:bg-slate-100"
              >
                <td class="whitespace-nowrap px-6 py-4">
                  <p class="font-bold subpixel-antialiased text-sky-700">{{ i.code }}</p>
                  
                </td>
                <td class="px-6 py-4">
                    <p class="font-light underline decoration-2 uppercase text-slate-500/100 text-right">{{ i.description }}</p>
                    
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

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


