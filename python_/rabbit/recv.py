
from kombu import Connection
from kombu.messaging import Consumer
from entity import task_queue

#rabbit_host = 10.120.120.11
#rabbit_port = 5672
#rabbit_userid = 'guest'
#rabbit_password = 'guest'
connection = Connection('amqp://guest:guest@10.120.120.11:5672//')
channel = connection.channel()

def process_media(body, message):
    print body
    message.ack()

# consume
import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
consumer = Consumer(channel, task_queue)
consumer.register_callback(process_media)
consumer.consume()

while True:
    connection.drain_events()

