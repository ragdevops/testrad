FROM ubuntu:latest
ENV VERSION 1.2.0
RUN apt-get update && \apt-get install -y python3 
RUN vim zip unzip && \ apt-get clean && \ rm -rf /var/lib/apt/list/*
COPY zip_job.py /tmp/
CMD echo "OS type and architecture : "$(unmae -srm) && \ echo "Verifying /tmp/zip_job.py exists:"&& \ ls- l /tmp/zip_job.py
