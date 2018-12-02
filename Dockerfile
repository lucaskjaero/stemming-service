FROM python:3.7-alpine3.8
COPY . /app/
WORKDIR /app
RUN apk add g++
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "StemmingService:app", "-b", ":8000"]
