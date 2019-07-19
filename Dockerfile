FROM python:3

ADD findmacvend.py /

RUN pip install requests

CMD [ "python3", "./findmacvend.py" ]

