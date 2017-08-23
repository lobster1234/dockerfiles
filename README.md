# dockerfiles
Dockerfiles for various needs

# Usage

1. Clone this repo, cd to the folder you'd want to build an image from.

```
bash-3.2$ cd solr
bash-3.2$ docker build .
Sending build context to Docker daemon  2.048kB
Step 1/6 : FROM java:8-jdk
 ---> d23bdf5b1b1b
Step 2/6 : WORKDIR /tmp
 ---> Using cache
 ---> 403329ba78b4
Step 3/6 : RUN wget http://archive.apache.org/dist/lucene/solr/6.5.1/solr-6.5.1.tgz
 ---> Using cache
 ---> d55015c1f566
Step 4/6 : RUN tar xvfz solr-6.5.1.tgz
 ---> Using cache
 ---> 8d3aebbe2b61
Step 5/6 : EXPOSE 8983
 ---> Running in 207c5b8c38eb
 ---> c594dac0f4f2
Removing intermediate container 207c5b8c38eb
Step 6/6 : CMD /tmp/solr-6.5.1/bin/solr start -force -f
 ---> Running in 81ddacfe080d
 ---> 32cff9e8ecd1
Removing intermediate container 81ddacfe080d
Successfully built IMAGE_ID
```
2. Make a note of the `IMAGE_ID` from the `docker build .` output

3. Look at the Dockerfile to see the port(s) exposed, like `solr` exposes `8983`, or `tomcat8` exposes `8080`

4. Start a container with port mapping. You can then use localhost:port to interact with the container over HTTP or any other protocol. This example will allow you to view the Solr Web Console on http://localhost:9999

`bash-3.2$ docker run -p9999:8983 IMAGE_ID`

5. To stop the container (`^C` is not going to work!), open another terminal. Look for the CONTAINER_ID and use `docker stop` with that CONTAINER_ID.

```
bash-3.2$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
b7502212946d        32cff9e8ecd1        "/bin/sh -c '/tmp/..."   About a minute ago   Up About a minute   0.0.0.0:9999->8983/tcp   brave_keller

bash-3.2$ docker stop b7502212946d
```

Enjoy!
