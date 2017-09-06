FROM python:3.6.2-alpine3.6
RUN pip install flask flask-restful
COPY api.py /tmp
EXPOSE 5000
CMD python /tmp/api.py
