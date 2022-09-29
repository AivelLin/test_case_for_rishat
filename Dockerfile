FROM python:3.10.7-slim
MAINTAINER Pavel Lomonosov 'aivellinsom@gmail.com'
WORKDIR /app
COPY . .
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir