FROM python:3.10-bullseye

COPY requirements.txt /tmp/
COPY mobile.py /tmp/
RUN pip install --requirement /tmp/requirements.txt

CMD ["python", "tmp/mobile.py"]

