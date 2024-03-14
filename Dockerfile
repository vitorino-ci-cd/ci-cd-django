FROM python:3.11.4-buster
RUN mkdir /code-vitorino
WORKDIR /code-vitorino
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "gunicorn --bind 0.0.0.0:8000 app.wsgi" ]