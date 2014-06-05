#! -*- coding:cp936 -*-
# entity.py

from kombu import Exchange, Queue

#定义了一个exchange
task_exchange = Exchange('tasks', type='direct')

#在这里进行了exchange和queue的绑定，并且指定了这个queue的routing_key
task_queue = Queue('piap', task_exchange, routing_key='suo_piao')
