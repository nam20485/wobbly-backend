FROM python:3.7.0-stretch
MAINTAINER Nathan Miller <nmiller217@gmail.com>
ENV PYTHONUNBUFFERED 1

# create and populate /code
RUN mkdir /code
WORKDIR /code

COPY /requirements.txt /code/
RUN pip install -r requirements.txt

RUN python
COPY . /code/