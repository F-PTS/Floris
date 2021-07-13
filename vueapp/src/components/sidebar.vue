<template>
  <div>
      <div class="background">
            <div class="WeLovePlants">
                <h1>We love plants</h1>
                <h3>but we have a lot of things on our minds</h3>
                
                <div class="line"></div>

                <p>
                People tend to forget about a lot of things.
                Perhaps you just forgot where did put your keys,
                when is your cousins birthday or
                <span>
                when was the last time you’ve watered your plants.
                </span>
                <br />
                <br />
                There are just a lot of things to remember.
                </p>
            </div>

            <div class="ButThenFloris">
                <h1>But then... <span>Floris</span></h1>
                <h3>we value your time and mental peace</h3>

                <p>
                That’s why we have developed <span>Floris</span>.
                To keep things simple and grow your plants for you.
                After adding your plants to the portfolio you will have
                to remember about your floral friends only if needed.
                </p>

                <div class="line"></div>

                <p>
                For each time you keep your watering day dead-line
                you will be rewarded with points that you can
                use in order to add more plants to your profile
                </p>

                <div class="linkButton" @click="handleClick()">
                    <router-link to="/why-bother"> <button>why bother?</button> </router-link>
                </div>
            </div>
      </div>
  </div>
</template>

<script>
export default {
    methods: {
        handleClick() {
            this.$root.isWhyActive = true;
            this.$root.flexControl('Why');
        }
    }
}
</script>

<style lang="scss" scoped>
.background {
    width: 1400px;
    height: 100vh;
    background-color: #1D1D1D;
    position: absolute;
    right: 0;
    overflow-y: scroll;
    scroll-behavior: smooth;

    scroll-snap-type: y mandatory;
}

.WeLovePlants, 
.ButThenFloris {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    scroll-snap-align: start;
}

h1 {
    font-family: Poppins;
    font-style: normal;
    font-weight: 600;
    font-size: 64px;
    line-height: 96px;

    margin-bottom: 17px;
    margin-top: 121px;

    color: white;
}

h3 {
    font-family: Poppins;
    font-style: normal;
    font-weight: 600;
    font-size: 32px;
    line-height: 48px;

    color: white;
}

p {
    width: 671px;
    height: 217px;

    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 24px;
    line-height: 36px;

    text-align: center;
        
    color: white;
}

.line {
    background: white;
    height: 2px;
    width: 69px;

    margin: 55px 0;
}

span {
    color: #729971
}

.WeLovePlants {
    
    .line {
        margin: 103px 0;
    }

}

.ButThenFloris {
    h1 {
        margin-top: 50px;
    }

    h3:nth-child(1) {
        margin-bottom: 138px;
    }

    h3:nth-child(2) {
        margin-bottom: 135px;
    }

    a > button {
        margin-bottom: 80px;
        padding: 12px 31px;
        background: #729971;
        border: none;
        color: white;
        font-size: 16px; 
    }
}
</style>