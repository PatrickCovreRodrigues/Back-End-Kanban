FROM bitnami/python:3.13

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD python -m uvicorn fast_zero:app --host 0.0.0.0 --port 8000 --reload
