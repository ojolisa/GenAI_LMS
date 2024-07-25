// store.js
import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
    state: {
        weeks: [],
        progassg: [],
    },
    mutations: {
        // define your mutations here
        setWeeks(state, weeks) {
            state.weeks = weeks;
        },
        setProgAssg(state, progassg) {
            state.progassg = progassg;
        }
    },
    actions: {
        // define your actions here
        async fetchWeeks({ commit }) {
            try {
                const response = await axios.get('http://localhost:5000/info');
                commit('setWeeks', response.data);
            } catch (error) {
                console.error(error);
            }
        },
        async fetchProgAssg({ commit }) {
            try {
                const response = await axios.get('http://localhost:5000/progassg');
                commit('setProgAssg', response.data);
            } catch (error) {
                console.error(error);
            }
        }
    },
    getters: {
        getLectureById: (state) => (id) => {
            for (let week of state.weeks) {
                for (let lecture of week.lectures) {
                    if (lecture.id == id) {
                        return lecture;
                    }
                }
            }
            return null;
        },
        getAssignmentById: (state) => (id) => {
            for (let week of state.weeks) {
                if (week.assignments) {
                    for (let assignment of week.assignments) {
                        if (assignment.id == id) {
                            return assignment;
                        }
                    }
                }
            }
            return null;
        },
        getProgAssgById: (state) => (id) => {
            return state.progassg.find(prog => prog.id == id);
        }
    }
})