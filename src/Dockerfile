FROM python:3.7
ADD . /people
WORKDIR /people
ENV IN_DOCKER_CONTAINER True
RUN pip install -r docker-dependencies.txt
