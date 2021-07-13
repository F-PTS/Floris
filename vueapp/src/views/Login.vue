<template>
  <div class="container">
    <form method="POST" action="./greeting-page">
      <h1>{{ errorMessage }}</h1>
      <input v-model="userEmail" type="email" placeholder="type your email" name="login_email" id="email">
      <input v-model="userPassword" type="password" placeholder="and now password" name="login_password" id="password">

      <div class="CreateAccount">
        <h3>Don't have an account yet?</h3>
        <router-link to="/register">create one here</router-link>
      </div>

      <input class="button" @click="handleUserInput($event)" type="submit" value="fufil potential">
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userEmail: '',
      userPassword: '',
      errorMessage: ''
    }
  },
  methods: {
    handleUserInput(event) {
      if(!this.userEmail || !this.userPassword) {
        event.preventDefault();
        return this.errorMessage = "One of the input fields are invalid"
      }

      event.target.submit()
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  .CreateAccount {
    font-size: 8px;
    margin: 48px 0;
  }

  .CreateAccount, form {
    display: flex;
    flex-direction: column;
    align-items: center;

    input {
      border: none;
      background: none;
      text-align: center;
      outline: none;
      padding: 8px 0;
      color: rgba(29, 29, 29, 0.25);
      border-bottom: 2px solid rgba(29, 29, 29, 0.25);
      transition: 0.2s;
      font-size: 16px;
      margin-top: 36px;
    }

    input:focus {
      color: rgb(29, 29, 29);
      border-bottom: 2px solid rgb(29, 29, 29);
    }

    .button {
      margin: 0;
      font-size: 10px;
      padding: 14px 42px;
      border: 1px solid #1d1d1d;
      border-radius: 5px;
      outline: none;
      width: min-content;
      color: #1d1d1d;
    }

    .button:hover {
      background: #1d1d1d;
      color: white;
    }
  }

}
</style>