<template>
  <div class="home">
     <div class="background"></div>
    <HeroText 
      msg="Keep your plants healthy!" 
      bottomText="Floris is a simple website that you can use to keep tracking<br />of your plants! Never miss your watering day. Add how<br />many plants you want and score points for keeping your<br />plants hydrated!"
    />
    <TwoLines class="TwoLines"></TwoLines>
  </div>
</template>

<script>
import HeroText from '@/components/HeroText.vue'
import TwoLines from '@/components/twoLines.vue'

export default {
  name: 'Home',
  components: {
    HeroText,
    TwoLines
  }
}

</script>

<style lang="scss" scoped>
  .background {
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background-image: url('../assets/image.png');
    background-repeat: no-repeat;
    background-position-x: 90%;
    background-position-y: 15%;
    background-size: 70%;
    position: absolute;
    top: 0;
  }

  .TwoLines {
    right: 40px;
  }
</style>