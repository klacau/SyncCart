import { createApp } from 'vue';
import './style.css';
import App from './App.vue';

import { createWebHistory, createRouter } from 'vue-router';

import HomePage from './components/WelcomePage.vue';
import WelcomePage from './components/WelcomePage.vue';
import SignUpPage from './components/SignUpPage.vue';

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
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach(async (to, from, next) => {
    if (to.name === 'Welcome' || to.name === 'SignUp' || to.name === 'SignIn') {
        console.log(to.name)
        next();
    } 
    else next({name: 'Welcome'});
})

createApp(App)
    .use(router)
    .mount('#app');
