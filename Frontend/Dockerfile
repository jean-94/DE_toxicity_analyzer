FROM python:3.8
WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update
RUN pip install flask
RUN pip install requests

COPY * ./

EXPOSE 5001
CMD ["flask", "run"]
