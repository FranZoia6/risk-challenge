# Imagen base de Python
FROM python:3.10


WORKDIR /app

COPY index.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "index.py"]

