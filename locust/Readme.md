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
## Access Locust on browser
Open browser and ponit it to http://localhost:8089

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

## Access locust on browser
```
$ docker inspect <container-id> | grep IPAddress

        "SecondaryIPAddresses": null,
        "IPAddress": "172.17.0.3",
        "IPAddress": "172.17.0.3",
 ```
 Now, open locust on browser at http://172.17.03:8089 
 
# 3. Locust Web Interface
#### Login Page (Local Run):

![alt text](https://github.com/limbuu/compare-loadtesting-tools/blob/main/locust/images/locust-local-WI.png)

#### Login Page (Docker Run):
![alt text](https://github.com/limbuu/compare-loadtesting-tools/blob/main/locust/images/locust-docker-WI.png)

#### Stats Page: 
![alt text](https://github.com/limbuu/compare-loadtesting-tools/blob/main/locust/images/locust-stats.png)

#### Chart Page: 
![alt text](https://github.com/limbuu/compare-loadtesting-tools/blob/main/locust/images/locust-chart.png)


# More Information on Locust:
### Website: https://locust.io/
### Documentation: https://docs.locust.io/
### Github: https://github.com/locustio/locust




