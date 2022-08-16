FROM python:3.7 AS builder
WORKDIR /build
# Add dependencies to run test during build
#RUN python -m pip install --upgrade pip
#RUN pip3 install -r dev-requirements.txt
#RUN pip3 install -r requirements.txt
COPY . .
RUN python setup.py build sdist bdist_wheel


FROM python:3.7
WORKDIR /dist
RUN apt-get -y update && apt-get -y upgrade
RUN python -m pip install --upgrade pip
