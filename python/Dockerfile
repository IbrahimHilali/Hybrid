FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./python/requirements/development.txt /app/
RUN pip install --no-cache-dir -r development.txt
COPY ./app/ /app/