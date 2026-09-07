FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask gunicorn

EXPOSE 10000

CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
