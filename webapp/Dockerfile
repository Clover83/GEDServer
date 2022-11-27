# pull official base image
FROM python:3.10.8-alpine3.16

# set work directory inside container
WORKDIR /usr/src/app

# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevent python from buffering to stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
