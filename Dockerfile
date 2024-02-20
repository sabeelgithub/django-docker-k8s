FROM python:3.11.8 as python-django
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","manage.py","runserver"]