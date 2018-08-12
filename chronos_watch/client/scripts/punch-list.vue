<template>
<div class="punch-list">
    <div class=""
        v-for="(punch, i) in punches"
        :key="i"
    >
        <p>{{ punch.timestamp }}</p>
        <button>X</button>
    </div>
</div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';


let API_PATH: string = 'http://localhost:8000/api/';

@Component
export default class PunchList extends Vue {
    punches: object[] = [];

    constructor() {
        super();
        this.loadPunches();
    }

    async loadPunches() {
        this.punches = await getPunches();
    }
};

async function getPunches(): Promise<object[]> {
    let res: Response = await fetch(API_PATH + 'punch');
    return (await res.json()).punches;
}

</script>


<style lang="sass">
$bg-color: #aaa;

.punch-list {
    background-color: #aaa;
}


</style>
