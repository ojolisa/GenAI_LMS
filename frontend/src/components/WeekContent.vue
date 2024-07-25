<template>
  <li>
    <div class="week-header" @click="toggleDropdown">
      <span>{{ week.name }}</span>
      <span class="arrow" :class="{ open: isOpen }">▼</span>
    </div>
    <ul v-if="isOpen" class="dropdown">
      <li
        v-for="lecture in week.lectures"
        :key="lecture.id"
        @click="selectLecture(lecture)"
      >
        {{ lecture.name }}
      </li>
      <li
        v-for="assignment in week.assignments"
        :key="assignment.id"
        @click="selectAssignment(assignment)"
      >
        {{ assignment.name }}
      </li>
      <li
        v-for="prog in filteredProgAssg"
        :key="prog.id"
        @click="selectProgAssg(prog)"
      >
        {{ prog.name }}
      </li>
      <li @click="selectWeekHelper">Week {{ week.id }} Helper</li>
    </ul>
  </li>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "WeekContent",
  components: {},
  props: {
    week: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapState(["progassg"]),
    filteredProgAssg() {
      // Filter progassg based on the current week.id
      return this.progassg.filter((prog) => prog.week_id === this.week.id);
    },
  },
  data() {
    return {
      isOpen: false,
    };
  },
  methods: {
    toggleDropdown() {
      this.isOpen = !this.isOpen;
    },
    selectLecture(lecture) {
      this.$router.push(`/lecture/${lecture.id}`);
    },
    selectAssignment(assignment) {
      this.$router.push(`/assignment/${assignment.id}`);
    },
    selectWeekHelper() {
      this.$router.push(`/week/${this.week.id}/helper`);
    },
    selectProgAssg(prog) {
      // New method for ProgAssg
      this.$router.push(`/progassg/${prog.id}`);
    },
  },
};
</script>

<style scoped>
.week-header {
  cursor: pointer;
  padding: 10px 15px;
  background-color: #2c3e50;
  border-bottom: 1px solid #34495e;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #ecf0f1;
  font-size: 16px;
  font-weight: 500;
}

.week-header:hover {
  background-color: #34495e;
  transition: background-color 0.3s ease-in-out;
}

.arrow {
  transition: transform 0.3s;
}

.arrow.open {
  transform: rotate(180deg);
}

.dropdown {
  list-style-type: none;
  padding: 0;
  margin: 0;
  background-color: #34495e;
}

.dropdown li {
  padding: 10px 15px;
  border-bottom: 1px solid #2c3e50;
  color: #ecf0f1;
  font-size: 14px;
}

/* Added transition for smoother hover effect */
.dropdown li:hover {
  background-color: #2c3e50;
  transition: background-color 0.3s ease-in-out;
}
</style>
