<template>
  <div class="assignment-view">
    <h2>{{ assignment.name }}</h2>
    <br /><br />
    <div
      class="question"
      v-for="(question, index) in assignment.questions"
      :key="index"
    >
      <p class="question-text">{{ index + 1 }}. {{ question.question }}</p>
      <ul class="options">
        <li
          class="option"
          v-for="(option, index) in question.options"
          :key="index"
        >
          <button
            @click="selectOption(question, option)"
            :class="{
              'selected-option': selectedAnswers[question.id] === option,
            }"
          >
            {{ option }}
          </button>
        </li>
      </ul>
      <hr />
      <!-- Horizontal line after each question -->
    </div>
    <button class="submit-button" @click="submitAnswers">Submit</button>
    <br /><br />
    <div v-if="data.message">
      <h3>Your Score:</h3>
      <p>{{ data.score }}</p>
      <br />
      <h3>Feedback:</h3>
      <div v-html="markdownedApiResponse"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MarkdownIt from "markdown-it";

export default {
  name: "AssignmentView",
  data() {
    return {
      md: new MarkdownIt({ breaks: true }),
      selectedAnswers: {},
      data: {},
    };
  },
  computed: {
    markdownedApiResponse() {
      return this.md.render(this.data.message);
    },
  },
  watch: {
    $route: "fetchAssignment",
  },
  created() {
    this.fetchAssignment();
    this.$store.dispatch("fetchQuestions");
  },
  methods: {
    fetchAssignment() {
      const assignmentId = this.$route.params.id;
      this.assignment = this.$store.getters.getAssignmentById(assignmentId);
    },
    selectOption(question, option) {
      this.selectedAnswers[question.id] = option;
    },
    async submitAnswers() {
      try {
        const response = await axios.post(
          "http://localhost:5000/submit_assg",
          this.selectedAnswers
        );
        this.data = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.assignment-view {
  padding: 20px;
}

.question {
  margin-bottom: 20px;
}

.question-text {
  font-weight: bold;
  margin-bottom: 10px;
}

.options {
  margin-left: 20px;
}

.option {
  margin-bottom: 5px;
}

.option button {
  margin: 5px;
  padding: 5px;
}

.selected-option {
  background-color: #4caf50; /* for example */
  color: white;
}

.submit-button {
  background-color: green;
  color: white;
  padding: 10px 20px;
  font-size: 1.2em;
  float: right;
  border: none;
  cursor: pointer;
}
</style>
