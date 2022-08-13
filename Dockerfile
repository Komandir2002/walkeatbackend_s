FROM python:3.10.4

WORKDIR /back_walkeat

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ['python', 'manage.py', 'runerver']