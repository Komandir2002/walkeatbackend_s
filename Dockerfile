FROM python:3.10.4

RUN mkdir -p /opt/services/walkeat
WORKDIR /opt/services/walkeat

RUN mkdir -p /opt/services/walkeat/requirements

ADD requirements.txt /opt/services/walkeat/

COPY . /opt/services/walkeat/

RUN pip install -r requirements.txt

