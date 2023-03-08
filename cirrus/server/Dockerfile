FROM python:3.11.2-slim-buster
WORKDIR /usr/src/cirrus
COPY cirrus/server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "cirrus.main:app", "--host", "0.0.0.0", "--port", "8001"]