FROM python:3.5

ENV DOCKERFILE_VERSION 1
ENV PYTHONBUFFERED 1
ENV APPLICATION_ROOT /webapp/

RUN apt-get update
RUN apt-get install -y build-essential git
RUN apt-get install -y nginx supervisor

RUN mkdir -p $APPLICATION_ROOT
ADD . $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run cp deploy/nginx-app.conf /etc/nginx/sites-enabled/
run cp deploy/supervisor-app.conf /etc/supervisor/conf.d/
run cp deploy/local_settings.py $APPLICATION_ROOT/webapp/

RUN pip install uwsgi
RUN pip install -r requirements.txt

RUN python3 manage.py collectstatic --noinput

expose 80
cmd ["supervisord", "-n"]



