ARG PYTHON_VERSION=3.9.6
FROM python:${PYTHON_VERSION} as base

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD python3 service/app.py --vault_addr "http://host.docker.internal:8200" --port 6379 --token "hvsvio2dl8SxHJU83uFk8O8JGGE"