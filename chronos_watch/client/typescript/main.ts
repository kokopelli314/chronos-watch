let API_PATH: string = 'http://localhost:8000/api/';

async function printPunches(): Promise<string> {
    let res: Response = await fetch(API_PATH + 'punch');
    let text: string = await res.text();
    console.log(text);
    return text;
}

async function postPunch() {
    let punch = {
        timestamp: new Date(),
        punch_type: 'in'
    };
    await fetch(API_PATH + 'punch', { 
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

printPunches();
postPunch();