<template>
  <div>
    <h1>CSV File Upload</h1>
    <input type="file" @change="handleFileUpload" accept=".csv" />
    <button @click="uploadFile">Upload</button>
    <p v-if="uploadStatus">{{ uploadStatus }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
    };
  },
  computed: {
    uploadStatus() {
      return this.$store.getters.getUploadStatus;
    },
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    uploadFile() {
      if (!this.selectedFile) {
        console.error("Please select a CSV file.");
        return;
      }
      this.$store.dispatch("uploadCSV", this.selectedFile);
    },
  },
};
</script>
