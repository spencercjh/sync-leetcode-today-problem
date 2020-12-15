FROM python:latest

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /

CMD ["python", "/main.py"]
