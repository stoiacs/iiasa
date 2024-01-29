import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from "@/views/RegisterView.vue";
import LoginView from "@/views/LoginView.vue";
import ProfileView from "@/views/ProfileView.vue";
import store from "@/store";
import CsvUpload from "@/views/CsvUpload.vue";
import AnalyzeView from "@/views/AnalyzeView.vue";
import TemperatureView from "@/views/TemperatureView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/csv-upload',
        name: 'CsvUpload',
        component: CsvUpload,
        meta: { requiresAuth: true },
    },
    {
        path: '/analyze',
        name: 'Analyze Data',
        component: AnalyzeView,
        meta: { requiresAuth: true },
    },
    {
        path: '/temperature',
        name: 'Historical climate data',
        component: TemperatureView,
        meta: { requiresAuth: true },
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        meta: { requiresAuth: true },
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, _, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.getters.isAuthenticated) {
            next();
            return;
        }
        next('/login');
    } else {
        next();
    }
});

export default router
