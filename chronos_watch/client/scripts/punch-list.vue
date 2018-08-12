<template>
<div>
    <div v-for="(punch, i) in punches"
        :key="i"
    >
        <p>{{ punch.timestamp }}</p>
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

    // mounted: async function() {
    //     let x = await getPunches();
    //     console.log(x)
    // }
};

async function getPunches(): Promise<Array<object>> {
    let res: Response = await fetch(API_PATH + 'punch');
    return (await res.json()).punches;
}


</script>

<style>

</style>
