FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python python3-pip
RUN apt-get update && apt-get install -y cowsay
RUN pip install cowsay
COPY app.py /app/
ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=8080
