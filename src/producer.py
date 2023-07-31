"""Producer code"""
import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='letterbox')
msg = "Jai Mata Di!, this is my first MQ message..."
channel.basic_publish(exchange='',
                      routing_key='letterbox',
                      body=msg)
print(f"sent message: {msg}")
connection.close()
