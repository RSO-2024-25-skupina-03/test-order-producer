FROM python:3.11-alpine

RUN pip install --no-cache-dir pdm
COPY src/test_order_producer /app/src/test_order_producer
COPY pdm.lock /app
COPY pyproject.toml /app

WORKDIR /app/
RUN pdm install --check --prod --no-editable

EXPOSE 8080

CMD ["pdm", "api"]
