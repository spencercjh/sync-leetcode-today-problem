FROM python:latest

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /

CMD["pytest"]

CMD ["python", "/main.py"]
