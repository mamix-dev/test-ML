# syntax=docker/dockerfile:1
FROM smizy/scikit-learn
WORKDIR /src
COPY /src /src
RUN pip install -r requirements.txt
