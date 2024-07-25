import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LectureView from './components/LectureView.vue'
import AssignmentView from './components/AssignmentView.vue'
import WeekHelper from './components/WeekHelper.vue'
import store from './store'
import HomePage from './components/HomePage.vue'
import ProgAssg from './components/ProgAssg.vue'

const routes = [
    { path: '/', name: 'HomePage', component: HomePage },
    { path: '/lecture/:id', component: LectureView },
    { path: '/assignment/:id', component: AssignmentView },
    { path: '/week/:id/helper', component: WeekHelper },
    { path: '/progassg/:id', component: ProgAssg }
]

const router = createRouter({
    history: createWebHistory(),
    routes // short for `routes: routes`
})

const app = createApp(App)
app.use(store)
app.use(router)

store.dispatch('fetchWeeks')
store.dispatch('fetchProgAssg')

app.mount('#app')