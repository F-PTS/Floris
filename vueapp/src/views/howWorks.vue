<template>
    <div class="HowItWorks">
      <div class="sideText">
        <h1>{{ sidetext }}</h1>
      </div>
      <SideBar class="sidebar"></SideBar>
      <TwoLines class="TwoLines"></TwoLines>
  </div>
</template>

<script>
import TwoLines from '@/components/twoLines.vue'
import SideBar from '@/components/sidebar.vue'

export default {
  data() {
    return {
      sidetext: "The problem"
    }
  },
  components: {
    TwoLines,
    SideBar
  },
  mounted() {
    document.querySelector('.sidebar').addEventListener('wheel', e => {
      if(e.deltaY < 0) {
        return this.sidetext = "The problem"
      }

      return this.sidetext = "The solution"
    });
  }
}


</script>

<style lang="scss" scoped>

  .HowItWorks {
    display: flex;
  }

  .sideText {
    width: 520px;
    height: 50%;

    position: relative;

    h1 {
      position: absolute;
      right: 0;
      font-size: 60px;
      transform: translate(40px, 160px) rotate(-90deg);
    }
  }

  .TwoLines {
    right: 1430px;
  }

  .HowItWorks {
    width: 100vw;
    height: 100vh;
    overflow: scroll;
  }
</style>