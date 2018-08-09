let API_PATH: string = 'http://localhost:8000/api/';

async function printPunches(): Promise<string> {
    let res: Response = await fetch(API_PATH + 'punch');
    let text: string = await res.text();
    console.log(text);
    return text;
}

async function postPunch() {
    let text: string = 'Hello worlds to the Falcon!';
    await fetch(API_PATH + 'punch', { 
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({ text: text })
     });
     console.log('posted')
}

printPunches();
postPunch();