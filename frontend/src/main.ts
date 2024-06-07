import { createApp } from 'vue';
import './style.css';
import App from './App.vue';

import { createWebHistory, createRouter } from 'vue-router';

import HomePage from './components/WelcomePage.vue';
import WelcomePage from './components/WelcomePage.vue';

const routes = [
    { 
        path: '/', 
        component: HomePage, 
        beforeEnter: (to, from) => {
            return { name: 'Welcome' };
        }
    },
    {
        path: '/welcome',
        name: 'Welcome',
        component: WelcomePage
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

createApp(App)
    .use(router)
    .mount('#app');
