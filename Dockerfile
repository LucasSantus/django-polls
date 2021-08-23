# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

RUN pip install --upgrade pip

# install psycopg2 dependencies
RUN apk update \
    && apk add mariadb-dev gcc python3-dev musl-dev libffi-dev openssl-dev jpeg-dev zlib-dev

# RUN apk update \
#     && apk add freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev graphviz \
#     cairo-dev pango-dev gdk-pixbuf-dev rust

# install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt
RUN pip install -r requirements-dev.txt

# copy project
COPY . /usr/src/app/