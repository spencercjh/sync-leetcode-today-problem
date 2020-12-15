FROM python:latest

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD main.py /main.py
ADD leetcode.py /leetcode.py

CMD ["python", "/main.py"]
