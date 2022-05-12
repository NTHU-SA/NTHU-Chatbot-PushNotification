FROM python:3.7-buster

WORKDIR /usr/src/app

ENV SERVER_IP=${GINIP}
ENV SERVER_PORT=8080
ENV SQLITE_DB=./sqlite.db
ENV LIST_DIRECTORY=./ActiveNotification/
ENV PERIOD=30

COPY . .

# RUN install sqlite3
RUN pip3 install -r requirements.txt
# RUN python3 initialize.py

CMD ["python3", "daemon.py"]
