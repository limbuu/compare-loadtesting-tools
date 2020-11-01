## Install Vegeta
### First, Install Go following link: https://golang.org/doc/install :
```
$ go version

go version go1.15.2 linux/amd64
```
There are two different ways of installing vegeta, you can install in either of the following ways
### 1. Installation from tar.gz file:
#### Download latest Vegeta binary
```
$ wget https://github.com/tsenart/vegeta/releases/download/cli%2Fv12.5.1/vegeta-12.5.1-linux-amd64.tar.gz
```
#### Unpack the binary and Move it into /usr/bin to make it available system-wide
```
$ tar xfz vegeta-12.5.1-linux-amd64.tar.gz
$ mv vegeta /usr/bin/vegeta
```
#### check installation
```
$ vegeta -version
Version: 
Commit: 
Runtime: go1.15.2 linux/amd64
Date: 
```

### 2. Installation as go module:
#### To avoid permission denied in /usr/bin path, run command:
```
$ sudo chown -R $USER:$USER /usr/local/go
```
#### Install as go module directly from github link
```
$ go get -u github.com/tsenart/vegeta
```
#### check installation
```
$ vegeta -version
Version: 
Commit: 
Runtime: go1.15.2 linux/amd64
Date: 
```

### Run Loadtest with Vegeta
```
$ echo "GET http://0.0.0.0:5000" | vegeta attack -duration=10s | tee results.bin | vegeta report

Requests      [total, rate, throughput]         500, 50.10, 50.09
Duration      [total, attack, wait]             9.982s, 9.98s, 2.217ms
Latencies     [min, mean, 50, 90, 95, 99, max]  1.001ms, 2.358ms, 2.237ms, 3.395ms, 3.592ms, 3.995ms, 4.471ms
Bytes In      [total, mean]                     6000, 12.00
Bytes Out     [total, mean]                     0, 0.00
Success       [ratio]                           100.00%
Status Codes  [code:count]                      200:500  
Error Set:

```


## More information on Vegeta
### Github: https://github.com/tsenart/vegeta
### Blog: https://www.scaleway.com/en/docs/vegeta-load-testing/