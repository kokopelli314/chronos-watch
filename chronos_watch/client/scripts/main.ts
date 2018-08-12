import PunchList from './punch-list.vue';
import Vue from 'vue';


let API_PATH: string = 'http://localhost:8000/api/';


async function postPunch() {
    let punch = {
        timestamp: new Date(),
        punch_type: 'in'
    };
    return await fetch(API_PATH + 'punch', { 
        method: 'POST',
        mode: 'cors',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(punch)
     });
     console.log('posted')
}

// printPunches();

let vm = new Vue({
    el: '#app',

    components: {
        'punch-list': PunchList
    },

    mounted: async function () {
        console.log('Vue mounted.');
        // console.log(await getPunches());
    }
});


