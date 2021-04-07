FROM python:3.9

WORKDIR /api 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
