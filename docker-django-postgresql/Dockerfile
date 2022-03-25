# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY docker/wait-for-it.sh /backend-app/

WORKDIR /backend-app
COPY src/requirements.txt /backend-app/

RUN pip install -r requirements.txt
# COPY . /backend-app/
RUN ls

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]