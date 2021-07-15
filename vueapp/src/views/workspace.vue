<template>
  <div class="workspace">
        <header>
            <h3>Hello, {{ username }}</h3>
            <div class="date">
                <h3>Today is {{ weekday() }}</h3>
            </div>
        </header>
        <div class="plantList">
            <ul>
                <li v-for="plant in APIData" :key="plant.id">
                    <div class="plantBox">
                        <div class="plantText">
                            <h1>{{ plant.id }}</h1>
                            <h2>{{ plant.name }} before watering</h2>
                        </div>
                    </div>
                </li>
            </ul>
            <button @click="addPlant(1, 'dupXDa', 2)">add plant</button>
        </div>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

class Plant {
    constructor(id, name, waterday) {
        this.id = id
        this.name = name;
        this.waterday = waterday;
    }
}

export default {
    data() {
        return {
            APIData: []
        }
    },
    methods: {
        addPlant(id, name, water) {
            this.plants.push(
                new Plant(name, water)
            )
        },
        weekday() {
            this.date = new Date();

            switch (this.date.getDay()) {
                case 1:
                    return "Monday"
                case 2:
                    return "Tuesday"
                case 3:
                    return "Wednesday"
                case 4:
                    return "Thursday"
                case 5:
                    return "Friday"
                case 6:
                    return "Saturday"
                case 7:
                    return "Sunday"
            }
        }
    }
}
</script>



<style lang="scss">
.plantList {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 100%;
    width: 100%;
}

ul {
    display: flex;
    flex-wrap: wrap;
    height: 80vh;
    width: 100vw;
    overflow-y: scroll;
}

.plantBox {
    width: 180px;
    height: 180px;
    background: #1d1d1d;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 24px;

    .plantText {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        h1 {
            font-weight: 600;
            font-size: 16px;
            line-height: 24px;
            color: white;
        }

        h2 {
            font-weight: normal;
            font-size: 14px;
            line-height: 21px;
            color: white;
        }
    }

}

li {
    text-decoration: none;
    list-style: none;
}
</style>