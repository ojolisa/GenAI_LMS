<template>
  <div class="week-helper">
    <h2>Week {{ id }} Helper</h2>
    <input
      type="text"
      v-model="userQuery"
      placeholder="Enter your query here"
    />
    <button @click="submitQuery">Submit</button>
    <div v-if="loading" class="loading-animation">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>
    <!-- <p v-else>{{ apiResponse }}</p> -->
    <div v-else v-html="markdownedApiResponse"></div>
  </div>
</template>

<script>
import axios from "axios";
import MarkdownIt from "markdown-it";

export default {
  name: "WeekHelper",
  data() {
    return {
      md: new MarkdownIt({ breaks: true }),
      id: null,
      userQuery: "",
      apiResponse: "",
      loading: false,
    };
  },
  computed: {
    markdownedApiResponse() {
      return this.md.render(this.apiResponse);
    },
  },
  watch: {
    $route: "fetchData",
  },
  created() {
    this.fetchData();
  },
  methods: {
    // Define your methods for handling user input and communicating with the backend here
    fetchData() {
      this.id = this.$route.params.id;
      this.userQuery = "";
      this.apiResponse = "";
      this.loading = false;
    },
    async submitQuery() {
      this.loading = true;
      try {
        const response = await axios.post("http://localhost:5000/helper", {
          query: this.userQuery,
          weekId: this.id,
        });
        this.apiResponse = response.data;
      } catch (error) {
        this.apiResponse = "An error occurred: " + error.message;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.week-helper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  font-family: Arial, sans-serif;
  min-height: 100vh; /* This will make the container take the full height of the viewport */
  width: 1400px; /* Define a width */
  margin: auto; /* Center the element horizontally */
}

.week-helper h2 {
  color: #333;
  margin-bottom: 20px;
}

.week-helper input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 500px; /* Increased width */
  margin-bottom: 10px;
}

.week-helper button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  margin-bottom: 10px;
}

.week-helper button:hover {
  background-color: #0056b3;
}

.week-helper .loading-animation {
  color: #007bff;
}

.week-helper p {
  color: #333;
  width: 500px; /* Increased width to match the input box */
  word-wrap: break-word;
}

.bar {
  width: 500px;
  height: 10px;
  background: linear-gradient(270deg, grey, white, grey);
  background-size: 200% 200%;
  margin: 5px 0;
  border-radius: 5px;
  animation: gradient 2s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 100% 0;
  }
  100% {
    background-position: -100% 0;
  }
}
</style>
