<template>
  <div id="app">
    <div class="sidebar">
      <Sidebar />
    </div>
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Sidebar from "./components/SideBar.vue";

export default {
  name: "App",
  components: {
    Sidebar,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  display: flex;
  min-height: 100vh;
  width: 100%;
}

.sidebar {
  flex: 0 0 300px;
  background-color: #333;
  color: white;
  overflow: auto;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  background-color: beige;
}
</style>
