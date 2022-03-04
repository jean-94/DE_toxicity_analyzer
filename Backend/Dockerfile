FROM python:3.6
WORKDIR ./
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install flask
RUN git clone https://github.com/unitaryai/detoxify
RUN pip install -e detoxify
COPY * ./
EXPOSE 5000
CMD ["flask","run"]
