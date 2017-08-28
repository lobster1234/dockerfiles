A simple python server that returns Hello World. Listens on port 8000.
```
$ docker build .                 
Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM ubuntu:latest
 ---> ccc7a11d65b1
Step 2/5 : RUN apt-get -y update && apt-get -y upgrade
 ---> Using cache
 ---> 9f7a29dd9dd8
Step 3/5 : RUN apt-get install -y python3  python3-pip
 ---> Using cache
 ---> f30540435740
Step 4/5 : COPY httpserver.py /tmp
 ---> b8b28ab01627
Removing intermediate container 26c9f1852c72
Step 5/5 : CMD python3 /tmp/httpserver.py
 ---> Running in d04496c28dad
 ---> af725b4baa11
Removing intermediate container d04496c28dad
Successfully built af725b4baa11

```
Run it with port mapping - 
```
$ docker run -p8000:8000 af725b4baa11
```
