import type { RouteRecordName } from 'vue-router';

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
];

const appTitle = 'SyncCart';

const routeTitles = new Map<RouteRecordName, string>([
    ['SignIn', `Вход | ${appTitle}`],
    ['SignUp', `Регистрация | ${appTitle}`],
    ['Welcome', `${appTitle}`],
]);

const getRouteTitle = (routeName: RouteRecordName) => routeTitles.get(routeName)!;

export const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach(async (to, _, next) => {
    if (authStore.accessToken || to.name === 'Welcome' || to.name === 'SignUp' || to.name === 'SignIn') {
        document.title = getRouteTitle(to.name!);
        next();
    } 
    else next({name: 'Welcome'});
});