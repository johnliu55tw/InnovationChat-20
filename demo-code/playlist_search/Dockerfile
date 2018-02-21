FROM python:alpine-3.6
MAINTAINER John Liu "johnliu@kkbox.com"
COPY . /app
RUN pip install /app

RUN mkdir -p /work/resources
WORKDIR /work

ENV FLASK_APP playlist_search
ENV FLASK_DEBUG true

CMD ["flask","run"]
