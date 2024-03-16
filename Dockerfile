FROM python:3.11.0-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main:app", "--reload", "--host=0.0.0.0"]
