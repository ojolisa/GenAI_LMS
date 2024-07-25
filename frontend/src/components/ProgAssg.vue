<template>
  <div class="code-editor">
    <br /><br />
    <p class="question">{{ prog.question }}</p>
    <hr />
    <MonacoEditor
      :value="code"
      @change="updateCode"
      language="python"
      :options="editorOptions"
      :width="800"
      :height="400"
      class="editor"
    ></MonacoEditor>
    <button class="submit-button" @click="submitCode">Submit</button>
    <div v-if="loading" class="loading-animation">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>
    <div v-else v-html="markdownedApiResponse"></div>
  </div>
</template>

<script>
import MonacoEditor from "monaco-editor-vue3";
import axios from "axios";
import MarkdownIt from "markdown-it";
import { mapGetters } from "vuex";

export default {
  name: "ProgAssg",
  components: {
    MonacoEditor,
  },

  data() {
    return {
      md: new MarkdownIt({ breaks: true }),
      prog: null,
      code: "",
      apiResponse: "",
      loading: false,
    };
  },
  watch: {
    $route: "fetchProg",
  },
  created() {
    this.fetchProg();
  },
  computed: {
    markdownedApiResponse() {
      return this.md.render(this.apiResponse);
    },
    ...mapGetters(["getProgAssgById"]),
  },
  methods: {
    fetchProg() {
      const progId = this.$route.params.id;
      this.prog = this.getProgAssgById(progId);
    },
    updateCode(newCode) {
      this.code = newCode;
    },
    async submitCode() {
      this.loading = true;
      try {
        const response = await axios.post(
          "http://localhost:5000/progassg_suggestions",
          {
            question: this.prog.question,
            code: this.code,
          }
        );
        this.apiResponse = response.data; // Store the API response
      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
}; // ...
</script>

<style>
.code-editor {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.question {
  margin-bottom: 20px;
  font-size: 20px;
  text-align: left;
  width: 100%;
  margin-left: 50px;
}

.editor {
  margin-bottom: 20px;
}

.submit-button {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.loading-animation {
  color: #007bff;
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
