<template>
  <div class="Text-Wrapper">
    <h1>{{ msg }}</h1>
    <p v-html="bottomText"></p>
    <div class="line"></div>
    <router-link to="/log-in" @click="handleClick()" class="buttonBox">
      <button>Get started</button>
      <div class="button_arrow">
        <svg width="32" height="16" viewBox="0 0 32 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="arrow">
          <path d="M31.7071 8.70711C32.0976 8.31658 32.0976 7.68342 31.7071 7.29289L25.3431 0.928932C24.9526 0.538408 24.3195 0.538408 23.9289 0.928932C23.5384 1.31946 23.5384 1.95262 23.9289 2.34315L29.5858 8L23.9289 13.6569C23.5384 14.0474 23.5384 14.6805 23.9289 15.0711C24.3195 15.4616 24.9526 15.4616 25.3431 15.0711L31.7071 8.70711ZM0 9L31 9V7L0 7L0 9Z" fill="#1D1D1D"/>
        </svg>
      </div> 
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HeroText',
  props: {
    msg: String,
    bottomText: String
  },
  methods: {
    handleClick() {
      this.$root.isLoginActive = true;
      this.$root.flexControl('Login');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  * {
    color: #1d1d1d;
  }

  .Text-Wrapper {
    margin-top: 100px;
  }

  h1 {
    font-size: 64px;
    font-weight: 600;
    margin-bottom: 31px;
    line-height: 96px;
  }

  p {
    font-size: 24px;
  }

  .line {
    height: 2px;
    width: 69px;
    background: #1d1d1d;
    margin: 40px 0 60px 0;
  }

  .buttonBox {
    display: flex;
    align-items: center;
    cursor: pointer;
    text-decoration: none;

    button {
      padding: 12px 38px;
      font-size: 24px;
      line-height: 36px;
      border: none;
      background: #729971;
      color: white;
      border-top-left-radius: 3px;
      border-bottom-left-radius: 3px;
    }

    .button_arrow {
      height: 60px;
      width: 60px;
      box-sizing: border-box;
      border: 2px #729971 solid;
      border-top-right-radius: 3px;
      border-bottom-right-radius: 3px;
      position: relative;

      .arrow {
        position: absolute;
        bottom: 50%;
        right: 50%;
        transform: translate(50%, 50%);
      }
    }
  }
</style>
