FROM tiangolo/uwsgi-nginx:python3.6
RUN pip install --upgrade pip
RUN pip install pipenv

ARG env=prod

COPY . /app
WORKDIR /app/
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 80
