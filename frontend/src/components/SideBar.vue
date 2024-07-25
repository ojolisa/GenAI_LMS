<template>
  <div class="sidebar">
    <ul>
      <WeekContent v-for="week in weeks" :key="week.id" :week="week" />
    </ul>
  </div>
</template>

<script>
import WeekContent from "./WeekContent.vue";
import { mapState } from "vuex";

export default {
  name: "SideBar",
  components: {
    WeekContent,
  },
  computed: {
    ...mapState(["weeks"]),
  },
};
</script>

<style scoped>
.sidebar {
  width: 300px;
  height: 100vh;
  background-color: #333;
  color: white;
  padding: 0;
  overflow-y: auto;
  top: 0;
  left: 0;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
