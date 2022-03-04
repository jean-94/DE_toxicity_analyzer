FROM python:3.8
WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update
RUN pip install flask

COPY * ./

EXPOSE 5000
CMD ["flask", "run"]