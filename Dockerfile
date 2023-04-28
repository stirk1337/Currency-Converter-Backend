FROM python:3.8

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r /app/requirements.txt

RUN pip install django

COPY . .

CMD python main.py