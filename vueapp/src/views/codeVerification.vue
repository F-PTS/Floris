<template>
  <div class="container">
    <form method="POST">
      <h1>{{ errorMessage }}</h1>
      <div class="code">
        <input v-model="first" type="text" placeholder="0" name="code_one" >
        <input v-model="second" type="text" placeholder="0" name="code_two">
        <input v-model="third" type="text" placeholder="0" name="code_three">
        <input v-model="fourth" type="text" placeholder="0" name="code_four">
        <input v-model="fifth" type="text" placeholder="0" name="code_five">
        <input v-model="sixth" type="text" placeholder="0" name="code_six">
        <input v-model="seventh" type="text" placeholder="0" name="code_seven">
      </div>
     
      <div class="email">
        <h3>No email?</h3>
        <router-link to="/code-verification">click here to resend</router-link>
        <router-link to="/register">click here to change email</router-link>
      </div>

      <router-link to="/workspace">
        <input class="button" @click="handleUserInput($event)" type="submit" value="verify">
      </router-link>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
        first: '',
        second: '',
        third: '',
        fourth: '',
        fifth: '',
        sixth: '',
        seventh: '',
        wholeUserCode: this.first + this.second + this.third + this.fourth + this.fifth + this.sixth + this.seventh,
        emailCode: '',
        errorMessage: ''
    }
  },
  methods: {
    handleUserInput(event) {
        if(this.wholeUserCode != this.emailCode) {
            event.preventDefault();
            return this.errorMessage = "The codes don't not match"
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

  .email {
    font-size: 8px;
    margin: 48px 0;
    flex-direction: column;
    display: flex;
    align-items: center;
  }

  form {
    display: flex;
    align-items: center;

    .code {
        align-items: center;

        input {
            width: 60px;

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
            margin-left: 48px;
        }

        input:focus {
            color: rgb(29, 29, 29);
            border-bottom: 2px solid rgb(29, 29, 29);
        }

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