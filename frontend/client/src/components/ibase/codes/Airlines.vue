<script>
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";

const CODES_QUERY = gql`
  query {
    getAirlines {
      id
      iata
      icao
      country
      commentEng
      commentRus
      description
      arlLogo
    }
  }
`;

export default {
  name: "AirlinesComp",
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
      getAirlines: "",
    };
  },
  apollo: {
    // Simple query that will update the 'hello' vue property
    getAirlines: CODES_QUERY,
  },
};
</script>

<template>
  <div class="overflow-x-auto">
    <div
      class="mb-3 pt-4 text-center text-lg transition-all duration-200 md:text-xl"
    >
      <span class="text-accent">A<span class="text-light uppercase">irlines </span></span>
      <span class="text-base-content text-bold">C<span class="text-bold uppercase">odes</span></span>
    </div>
    <table class="table w-full">
      <thead>
        <tr>
          <th>Airline</th>
          <th>Icao</th>
          <th>Country</th>
          <th>English</th>
          <th>Russian</th>
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
      <tbody v-for="i in result.getAirlines" v-else :key="i.id">
        <tr class="hover space-x-3">
          <td>
            <div class="flex items-center space-x-3">
              <div class="avatar">
                <div class="mask mask-squircle h-12 w-12">
                  <img :src="i.arlLogo" alt="{{ i.iata }}">
                </div>
              </div>
              <div>
                <div class="font-bold">
                  {{ i.commentEng }}
                </div>
                <div class="text-sm opacity-50">
                  {{ i.country }}
                </div>
              </div>
            </div>
          </td>
          <td>{{ i.icao }}</td>
          <td>{{ i.country }}</td>
          <td>{{ i.commentEng }}</td>
          <td>{{ i.commentRus }}</td>
          <td>{{ i.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
