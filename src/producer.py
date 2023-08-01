"""Producer code"""
import pika
import logging
from src import params as param
from src.consumer import consume_event 

def produce_event(msg):
    logging.warning("-------in produce event is : %s", msg)
    connection_params = pika.ConnectionParameters(host='172.17.0.2',port=5672)
    # connection_params = pika.ConnectionParameters(host='127.0.0.1',port=5672)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='letterbox')
   #msg = "Jai Mata Di!, this is my first MQ message..."
    # msg = '{ "service_id" : 1, "service_name" : "userSrv",  "event_type" : 1}'
    channel.basic_publish(exchange='',
                        routing_key='letterbox',
                        body=str(msg))
    print(f"sent message: {msg}")
    logging.warning("-------output is : %s", msg)
    connection.close()
