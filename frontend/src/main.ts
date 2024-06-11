import { createApp } from 'vue';
import './style.css';
import App from './App.vue';

import { createWebHistory, createRouter } from 'vue-router';

import HomePage from './components/HomePage.vue';
import WelcomePage from './components/WelcomePage.vue';
import SignUpPage from './components/SignUpPage.vue';
import SignInPage from './components/SignInPage.vue';

import { authStore } from './auth';

const routes = [
    { 
        path: '/', 
        name: 'Root',
        component: HomePage
    },
    {
        path: '/welcome',
        name: 'Welcome',
        component: WelcomePage
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUpPage
    },
    {
        path: '/sign-in',
        name: 'SignIn',
        component: SignInPage
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach(async (to, from, next) => {
    if (authStore.accessToken || to.name === 'Welcome' || to.name === 'SignUp' || to.name === 'SignIn') {
        next();
    } 
    else next({name: 'Welcome'});
})

createApp(App)
    .use(router)
    .mount('#app');
