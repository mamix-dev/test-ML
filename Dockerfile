# syntax=docker/dockerfile:1
FROM tensorflow/tensorflow
WORKDIR /src
COPY /src /src
RUN pip install -r requirements.txt
