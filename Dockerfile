FROM python:3

WORKDIR /code
EXPOSE 5001

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./python-server/ .
CMD ["python", "server.py"]
