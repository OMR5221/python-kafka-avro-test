FROM python:3.6

WORKDIR /usr/app

EXPOSE 9092
EXPOSE 8081

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

CMD ["python3", "consume_record.py"]
