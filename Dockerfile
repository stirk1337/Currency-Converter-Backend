FROM python

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r /app/requirements.txt

COPY . .

CMD python -u src/main.py