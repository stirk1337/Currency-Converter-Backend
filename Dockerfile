FROM python

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD python -u main.py
