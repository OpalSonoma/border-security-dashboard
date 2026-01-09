FROM python:3.10-slim

WORKDIR /app
COPY ml-backend.py .

RUN pip install fastapi uvicorn numpy --no-cache-dir

EXPOSE 5000
CMD ["uvicorn", "ml-backend:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
