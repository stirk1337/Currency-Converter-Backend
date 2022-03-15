FROM python

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . .

CMD ["python", "main.py"]