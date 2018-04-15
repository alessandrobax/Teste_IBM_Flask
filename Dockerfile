FROM ubuntu
#WORKDIR /app
#ADD . /Teste_Final
#WORKDIR /Teste_Final

RUN apt-get update
RUN apt-get install -y python-setuptools

RUN alias python="/usr/bin/python3.5"

RUN apt-get install -y python3-pip

RUN mkdir /opt/flask_app
WORKDIR /opt/flask_app
ADD requirements.txt /opt/flask_app/
RUN pip3 install -r requirements.txt
ADD . /opt/flask_app

WORKDIR /opt/flask_app

CMD [ "python", "app.py", "runserver" ]