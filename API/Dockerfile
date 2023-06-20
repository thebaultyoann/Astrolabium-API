FROM python:3.11.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

USER root 

RUN apt-get install gcc wget 
RUN wget https://dlm.mariadb.com/2678579/Connectors/c/connector-c-3.3.3/mariadb-connector-c-3.3.3-debian-buster-amd64.tar.gz -O - | tar -zxf - --strip-components=1 -C /usr 

ENV LD_LIBRARY_PATH=/usr/lib/mariadb 

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
