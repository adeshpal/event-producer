"""Producer code"""
import pika

def produce_event():
    connection_params = pika.ConnectionParameters(host='172.17.0.3',port=5672)
    # connection_params = pika.ConnectionParameters(host='127.0.0.1',port=5672)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='letterbox')
    msg = "Jai Mata Di!, this is my first MQ message..."
    channel.basic_publish(exchange='',
                        routing_key='letterbox',
                        body=msg)
    print(f"sent message: {msg}")
    connection.close()



produce_event()
