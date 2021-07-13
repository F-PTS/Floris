<template>
  <div id="App">
      <nav class="nav">
        <div @click="flexControl('Home'); isHomeActive = true" :class="ReverseHome"  class="Home Router marginBot">
            <router-link to="/">Home</router-link>
            <div :class="{ active: isHomeActive }" class="line"></div>
        </div>

         <div @click="flexControl('How'); isHowWorksActive = true" :class="ReverseHowWorks" class="HowWorks Router marginBot">
              <router-link to="/how-it-works">How it works</router-link>
              <div :class="{ active: isHowWorksActive }" class="line"></div>
        </div>

        <div @click="flexControl('Why'); isWhyActive = true" :class="ReverseWhy"  class="Why Router marginBot">
            <router-link to="/why-bother">Why bother?</router-link>
            <div :class="{ active: isWhyActive }" class="line"></div>
        </div>

         <div @click="flexControl('Login'); isLoginActive = true" :class="ReverseLogin" class="Login Router">
          <router-link to="/log-in">Log in</router-link>
          <div :class="{ active: isLoginActive }" class="line"></div>
        </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import store from '@/store/index.js'

export default {
  data() {
    return {
      isHomeReversed: true,
      isHowWorksReversed: false,
      isWhyReversed: false,
      isLoginReversed: false,

      isHomeActive: true,
      isHowWorksActive: false,
      isWhyActive: false,
      isLoginActive: false,
    }
  },
  store,
  methods: {
    flexControl(branch) {
      switch(branch) {
        case 'Home':

          this.isHowWorksReversed = false,
          this.isWhyReversed = false,
          this.isLoginReversed = false,

          this.isHowWorksActive = false,
          this.isWhyActive = false,
          this.isLoginActive = false,

          this.isHomeReversed = true
          break

        case 'How':
          this.isHomeReversed = false,
          this.isWhyReversed = false,
          this.isLoginReversed = false,

          this.isHomeActive = false,
          this.isWhyActive = false,
          this.isLoginActive = false,

          this.isHowWorksReversed = true;
          break

        case 'Why':

          this.isHomeReversed = false,
          this.isHowWorksReversed = false,
          this.isLoginReversed = false,

          this.isHomeActive = false,
          this.isHowWorksActive = false,
          this.isLoginActive = false,

          this.isWhyReversed = true
          break

        case 'Login':
          this.isHomeReversed = false,
          this.isHowWorksReversed = false,
          this.isWhyReversed = false,

          this.isHomeActive = false,
          this.isHowWorksActive = false,
          this.isWhyActive = false,

          this.isLoginReversed = true
          break

        default:
          this.isHomeReversed = true;
          break
      }
    }
  },
  computed: {
    ReverseHome() {
      return this.isHomeReversed ? 'reversedFlex' : 'flex'
    },

    ReverseHowWorks() {
      return this.isHowWorksReversed ? 'reversedFlex' : 'flex'
    },

    ReverseWhy() {
      return this.isWhyReversed ? 'reversedFlex' : 'flex'
    },

    ReverseLogin() {
      return this.isLoginReversed ? 'reversedFlex' : 'flex'
    }
  }
}
</script>

<style lang="scss">

  * {
    font-family: 'poppins';
    margin: 0px;
    color: #1d1d1d;
  }

  body {
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    background: #F8F7F5;
  }

  #App {
    width: 1780px; 
    margin: 0 40px 0 auto;
  }

  .flex {
    display: flex;
    align-items: center;
    transition: 0.3s;
  }

  .reversedFlex {
    transition: 0.3s;
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
    font-weight: 600;
  }

  .Router {
    transition: 0.2s;
    margin-bottom: 15px;
    
    &:hover {
      font-weight: 600;
      transition: 0.2s;
    }
  } 

  .nav {
    position: absolute;
    bottom: 72px;
    display: flex;
    flex-direction: column;

    a {
      text-decoration: none;
    }

    .line {
      width: 20px;
      height: 1px;
      background: #1d1d1d;
      margin-left: 13px;
    }

    .Home{
      .line {
        width: 101px;
      }
    }

    .HowWorks{
      .line {
        width: 50px;
      }
    }

    .Why {
      .line {
        width: 48px;
      }
    }

    .Login{
      .line {
        width: 102px;
      }
    }

    .active {
      transform: translateX(-13px);
    }
  }
</style>
