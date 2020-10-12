# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-alpine

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# App environment variables
ENV APP_DATABASE_URI=sqlite:////usr/db/test.db
ENV APP_SECRET_KEY=verysecretkey

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /web-app
COPY . /web-app

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]


