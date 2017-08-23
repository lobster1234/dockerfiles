FROM java:8-jdk
WORKDIR /tmp
RUN wget http://archive.apache.org/dist/lucene/solr/6.5.1/solr-6.5.1.tgz
RUN tar xvfz solr-6.5.1.tgz
EXPOSE 8983
CMD /tmp/solr-6.5.1/bin/solr start -force -f
# docker build . 
# Note the image ID
# docker run -p8983:8983 <imageid>
# point the browser to localhost:8983 for solr console
