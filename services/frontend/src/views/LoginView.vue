<template>
  <section>
    <form @submit.prevent="submit" class="col-3">
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input type="text" name="username" v-model="form.username" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" name="password" v-model="form.password" class="form-control" />
      </div>
      <p v-if="errorMessage" class="text-danger">{{ errorMessage }}</p>
      <button type="submit" class="btn btn-primary col-4">Login</button>
      <!-- eslint-disable-next-line vue/no-deprecated-router-link-tag-prop -->
      <router-link to="/register" tag="button" class="btn btn-secondary col-4 offset-4">Register</router-link>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'UserLogin',
  data() {
    return {
      form: {
        username: '',
        password:'',
      },
      errorMessage: ''
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      try{
        await this.logIn(User);
        this.$router.push('/');
      } catch (e) {
        this.errorMessage = e.response.data.detail || 'An error occurred';
      }
    }
  }
});
</script>