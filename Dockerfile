FROM python:alpine

COPY miip.py /miip.py

CMD ["python","miip.py"]
