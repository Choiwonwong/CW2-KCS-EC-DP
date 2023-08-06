FROM python:3.8

WORKDIR /app

COPY main.py /app/
COPY requirements.txt /app/
COPY templates /app/templates/
COPY routers /app/routers/
COPY models /app/models/
COPY database /app/database/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
