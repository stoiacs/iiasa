import 'bootstrap/dist/css/bootstrap.css';
import {createApp} from "vue";
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store';
import {VueCsvImportPlugin} from "vue-csv-import";

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5001/';

app.use(router);
app.use(store);
app.use(VueCsvImportPlugin)
app.mount("#app");
