import axios from 'axios';

const state = {
    uploadStatus: null,
};

const getters = {
    getUploadStatus: (state) => state.uploadStatus,
};

const actions = {
    async uploadCSV({commit}, file) {
        try {
            const formData = new FormData();
            formData.append("file", file);

            const response = await axios.post("/csv-data", formData);

            if (response.status === 200) {
                commit("SET_UPLOAD_STATUS", "success");
            } else {
                commit("SET_UPLOAD_STATUS", "error");
            }
        } catch (error) {
            console.error(error);
            commit("SET_UPLOAD_STATUS", "error");
        }
    },

};

const mutations = {
    SET_UPLOAD_STATUS(state, status) {
        state.uploadStatus = status;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};