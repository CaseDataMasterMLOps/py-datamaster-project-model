FROM python:3.12-slim

COPY ./requirements.txt /usr/requirements.txt
COPY ./src /usr/src
COPY ./models /usr/models

WORKDIR /usr

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "src/app/main.py" ]

