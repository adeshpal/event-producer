import pika
import logging
import json
from src.schema import EventInfo, Role,User, Admin


def consume_event():
    logging.warning("-------in consume event is : %s", "")

    connection_params = pika.ConnectionParameters(host='172.17.0.2',port=5672)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    def on_message_received(ch, method, properties, body):
        data = json.loads(body)
        logging.warning("received new message : %s", data)
        eventInfo = EventInfo(user_id=1, 
                              event_type=data.get('event_type',0),
                              service_id=data['service_id'] )


    channel.queue_declare(queue='letterbox')
    channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)
    logging.warning("starting consuming--->")
    channel.start_consuming()
