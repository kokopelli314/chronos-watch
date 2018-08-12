<template>
<div class="punch-list">
    <div class="row"
        v-for="(punch, i) in punches"
        :key="i"
    >
        <p>{{ punch.punch_type }}</p>
        <p>{{ punch.timestamp }}</p>
        <button
            @click="deletePunch(punch)"
        >X</button>
    </div>
</div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';

let API_PATH: string = 'http://localhost:8000/api/';


enum PunchType {
    'in',
    'out'
}

class Punch {
    id!: number;
    timestamp!: Date;
    punch_type!: PunchType;

    constructor(data: Partial<Punch>) {
        Object.assign(this, data);
    }

    static deserialize(json: object): Punch {
        return new Punch(json);
    }
}



@Component
export default class PunchList extends Vue {
    punches: Punch[] = [];

    constructor() {
        super();
        this.loadPunches();
    }

    async loadPunches() {
        this.punches = await getPunches();
    }

    async deletePunch(punch: Punch) {
        console.log(`Delete Punch ${punch.id}!`);
    }
};

async function getPunches(): Promise<Punch[]> {
    let res: Response = await fetch(API_PATH + 'punch');
    let list = (await res.json()).punches;
    return list.map(Punch.deserialize);
}

</script>


<style lang="sass">
$bg-color: #aaa;

.punch-list {
    background-color: #aaa;
}

.row {
    max-width: 500px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

</style>
