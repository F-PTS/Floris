<template>
    <div class="twoLinesBox">
        <div class="lineOne"></div>
        <div class="lineTwo"></div>
    </div>
</template>

<style lang="scss" scoped>
.twoLinesBox {
    display: flex;
    align-items: center;
    position: absolute;
    top: 50%;
    transform: translateY(-50%) ;

    .lineOne {
      height: 26px;
      width: 2px;
      margin-right: 20px;
      background-color: #1D1D1D;
    }

    .lineTwo {
      height: 69px;
      width: 2px;
      background-color: #1D1D1D;
    }
  }

</style>