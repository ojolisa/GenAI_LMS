<template>
  <div class="lecture-view">
    <h2>{{ lecture.name }}</h2>
    <br /><br />
    <iframe
      width="1120"
      height="630"
      :src="lecture.video"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
    <br /><br />
    <button class="summarize-button" @click="fetchSummary">Summarize</button>
    <div v-if="loading" class="loading-animation">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>
    <div v-if="summary" v-html="markdownedApiResponse"></div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
import MarkdownIt from "markdown-it";

export default {
  name: "LectureView",
  data() {
    return {
      md: new MarkdownIt({ breaks: true }),
      lecture: null,
      summary: "",
      loading: false,
    };
  },
  watch: {
    $route: "fetchLecture",
  },
  created() {
    this.fetchLecture();
  },
  computed: {
    ...mapGetters(["getLectureById"]),
    markdownedApiResponse() {
      return this.md.render(this.summary);
    },
  },
  methods: {
    fetchLecture() {
      const lectureId = this.$route.params.id;
      this.lecture = this.getLectureById(lectureId);
    },
    async fetchSummary() {
      this.loading = true;
      const lectureId = this.$route.params.id;
      try {
        const response = await axios.get(
          `http://localhost:5000/summary/${lectureId}`
        );
        this.summary = response.data;
      } catch (error) {
        this.summary = "An error occurred: " + error.message;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.lecture-view {
  padding: 20px;
}

.summarize-button {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  margin: 4px 2px;
  cursor: pointer;
  transition-duration: 0.4s;
  border-radius: 12px; /* Rounded corners */
}

.summarize-button:hover {
  background-color: #45a049;
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

iframe,
.summarize-button {
  display: block;
}
</style>
