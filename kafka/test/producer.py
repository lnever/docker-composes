# coding: utf-8
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')


while True:

    res = producer.send(topic='test_topic', value='233')
    time.sleep(1)

    print(res.value)
    time.sleep(1)
    producer.flush()
