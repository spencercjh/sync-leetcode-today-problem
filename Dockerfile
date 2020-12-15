FROM python:latest

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD main.py /main.py
ADD leetcode_client.py /leetcode_client.py
ADD leetcode_problem.py /leetcode_problem.py

CMD ["python", "/main.py"]
