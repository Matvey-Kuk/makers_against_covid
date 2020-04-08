FROM python:3.7-alpine

RUN apk add bash python3-dev build-base linux-headers pcre-dev mariadb-connector-c-dev openssl-dev libffi-dev git
RUN pip install uwsgi

WORKDIR /etc/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

CMD ["uwsgi", "--chdir=/etc/app", "--module=mac.wsgi:application", "--master", "--pidfile=/tmp/project-master.pid", "--http=0.0.0.0:8080", "--processes=5", "--uid=1000", "--gid=2000", "--harakiri=20", "--max-requests=5000", "--vacuum"]