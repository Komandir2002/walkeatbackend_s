FROM python:3

RUN mkdir -p /opt/services/walkeat
WORKDIR /opt/services/walkeat

RUN mkdir -p /opt/services/walkeat/requirements

ADD requirements.txt /opt/services/walkeat/


RUN pip install -r requirements.txt

