FROM python:3.9

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]