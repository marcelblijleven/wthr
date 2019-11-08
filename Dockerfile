FROM python:3

ADD . /app

RUN pip install -r app/requirements.txt

ENTRYPOINT ["python", "app/program.py"]
