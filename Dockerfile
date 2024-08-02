# Dockerfile
FROM mageai/mageai:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY pipeline/ pipeline/
COPY .env .env

CMD ["python", "pipeline/pipeline.py"]
