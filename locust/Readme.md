# 1. Local SetUp
## Create Environment 
```
$ virtualenv venv --python=python3.6
$ source venv/bin/activate
(venv)$ pip3 install -r requirements.txt

```
## Check Installation
```
$ locust -V

locust 1.1
```
## Run Loadtest script
```
$ locust -f locustfile.py
```

# 2. Docker Setup
Make sure, you have installed docker already. 
## Run the application to test as docker container
Build and run simple flask app as docker container from https://github.com/limbuu/compare-loadtesting-tools/tree/main/app
```
$ docker build -t test-app .
$ docker run -it -p 5000:5000 test-app
```
Get the IPAddress of the app docker container.
```
$ docker inspect <container-id> | grep IPAddress

        "SecondaryIPAddresses": null,
        "IPAddress": "172.17.0.3",
        "IPAddress": "172.17.0.3",

```
Use this as "host" in locustfile.py
```
host = "http://172.17.0.3:5000"
```

## Run locust as docker container, mounting locustfile
```
$ docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py
```

