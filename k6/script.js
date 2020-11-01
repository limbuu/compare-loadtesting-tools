// init code
import http from "k6/http"
import {sleep, check} from "k6"

export let options = {
    vus:10,
    duration:"1m"
};

// VU code
export default function(){
    let url = "http://0.0.0.0:5000";
    let res = http.get(url);
    check(res,{
        "status code is 200": (res)=> res.status==200
    });
    sleep(1)

};
