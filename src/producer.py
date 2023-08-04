"""Producer code"""
import logging as log
import json
import pika
import src.params as param

def produce_event(msg):
    """Producer method to produce event in audit queue"""
    try:
        log.warning("Got message to publish= %s", msg)
        connection_params = pika.ConnectionParameters(host=param.QUEUE_HOST,port=param.QUEUE_PORT)
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()

        channel.queue_declare(queue=param.QUEUE_NAME)
        data = json.dumps(msg)
        channel.basic_publish(exchange='',
                            routing_key=param.QUEUE_NAME,
                            body=data)
        log.warning("Successfully sent message=%s", msg)
        connection.close()
        return True
    except Exception as fault:
        log.error("Something went wrong, event may not be processed. Error=%s", fault)
    return False
