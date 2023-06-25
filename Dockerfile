FROM python:3.9.17-alpine3.18
EXPOSE 8001

WORKDIR /app
COPY . . 
RUN pip install -r requirements.txt
CMD uvicorn main:app --port 8001 --host 0.0.0.0