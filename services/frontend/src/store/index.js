import {createStore} from "vuex";

import users from './modules/users';
import csvdata from './modules/csvdata';

export default createStore({
    modules: {
        users,
        csvdata
    }
});