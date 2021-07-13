<template>
  <div class="container">
    <form method="POST">
      <h1>{{ errorMessage }}</h1>
      <input v-model="userEmail" type="email" placeholder="type your email" name="register_email" id="email">
      <input v-model="userName" type="text" placeholder="now your username" name="register_name" id="username">
      <input v-model="userPassword" type="password" placeholder="and the password" name="register_password" id="password">
       <input v-model="userRepeatedPassword" type="password" placeholder="repeat the password" name="register_email" id="repeatedpassword">

      <div class="LogIn">
        <h3>already have an account?</h3>
        <router-link to="/log-in">click here to login</router-link>
      </div>

      <router-link to="/code-verification">
        <input class="button" @click="handleUserInput($event)" type="submit" value="register">
      </router-link>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userEmail: '',
      userPassword: '',
      userRepeatedPassword: '',
      userName: '',
      errorMessage: ''
    }
  },
  methods: {
    handleUserInput(event) {
        if(!this.userEmail || !this.userPassword || !this.userRepeatedPassword || !this.userName ) {
            event.preventDefault();
            return this.errorMessage = "One of the input fields are invalid"
        }

      event.target.submit()
    }
  }
}
</script>

<style lang="scss">
.container {
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  .LogIn {
    font-size: 8px;
    margin: 48px 0;
  }

  .LogIn, form {
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