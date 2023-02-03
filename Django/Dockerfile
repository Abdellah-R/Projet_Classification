FROM python:3.9.12

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate 

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]