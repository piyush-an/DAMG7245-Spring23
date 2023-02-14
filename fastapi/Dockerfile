FROM python:3.10.6

# RUN RUN apt-get update &&  apt-get -y upgrade

RUN pip install --upgrade pip

WORKDIR /app

ADD main.py requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn" ,"-w", "4", "-k", "uvicorn.workers.UvicornWorker" , "--bind", "0.0.0.0:8000", "main:app"]