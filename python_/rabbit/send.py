# send.py

from kombu import Connection
from kombu.messaging import Producer
from entity import task_exchange
from kombu.transport.base import Message

connection = Connection('amqp://guest:guest@10.120.120.11:5672//')
channel = connection.channel()

message=Message(channel,body='Hello Kombu')

# produce
producer = Producer(channel,exchange=task_exchange)
producer.publish(message.body,routing_key='suo_piao')
import ipdb; ipdb.set_trace() ### XXX BREAKPOINT

