## Install K6
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
$ echo "deb https://dl.bintray.com/loadimpact/deb stable main" | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install k6
```
## Verify Installtion
```
$ k6 version

k6 v0.28.0 (2020-09-24T14:33:59+0000/v0.28.0-0-gdee9c4ce, go1.14.9, linux/amd64)
```
## Run Loadtesting Script
### With default configuration

```
$ K6 run script.js
```
### Run overriding the configuration
```
$ K6 run --vus 10 --duration 1m script.js
```

## Result as Standard Output
```
          /\      |‾‾| /‾‾/   /‾‾/   
     /\  /  \     |  |/  /   /  /    
    /  \/    \    |     (   /   ‾‾\  
   /          \   |  |\  \ |  (‾)  | 
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: script.js
     output: -

  scenarios: (100.00%) 1 scenario, 10 max VUs, 1m30s max duration (incl. graceful stop):
           * default: 10 looping VUs for 1m0s (gracefulStop: 30s)


running (1m00.3s), 00/10 VUs, 600 complete and 0 interrupted iterations
default ✓ [======================================] 10 VUs  1m0s

    ✓ status code is 200

    checks.....................: 100.00% ✓ 600  ✗ 0   
    data_received..............: 100 kB  1.7 kB/s
    data_sent..................: 47 kB   776 B/s
    http_req_blocked...........: avg=331.99µs min=64.52µs  med=354.65µs max=919.36µs p(90)=503.39µs p(95)=538.75µs
    http_req_connecting........: avg=199.66µs min=38.5µs   med=208.72µs max=424.93µs p(90)=309.42µs p(95)=326.53µs
    http_req_duration..........: avg=3.38ms   min=474.88µs med=2.72ms   max=22.52ms  p(90)=6.09ms   p(95)=9.05ms  
    http_req_receiving.........: avg=558.65µs min=23.31µs  med=334.22µs max=8.81ms   p(90)=969.34µs p(95)=1.84ms  
    http_req_sending...........: avg=119.49µs min=20.87µs  med=109.59µs max=898.4µs  p(90)=172.66µs p(95)=201.13µs
    http_req_tls_handshaking...: avg=0s       min=0s       med=0s       max=0s       p(90)=0s       p(95)=0s      
    http_req_waiting...........: avg=2.7ms    min=369.67µs med=2.18ms   max=21.87ms  p(90)=4.77ms   p(95)=6.06ms  
    http_reqs..................: 600     9.951475/s
    iteration_duration.........: avg=1s       min=1s       med=1s       max=1.02s    p(90)=1s       p(95)=1s      
    iterations.................: 600     9.951475/s
    vus........................: 10      min=10 max=10
    vus_max....................: 10      min=10 max=10

```

## For more information on K6
### Website: https://k6.io/
### Github: https://github.com/loadimpact/k6