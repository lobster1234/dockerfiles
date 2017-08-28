FROM ubuntu:latest
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3  python3-pip
COPY httpserver.py /tmp
CMD python3 /tmp/httpserver.py
