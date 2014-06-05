"""Spawn multiple workers and collect their results.

Demonstrates how to use the eventlet.green.socket module.
"""
import eventlet
from eventlet.green import socket

def geturl(url):
    c = socket.socket()
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    ip = socket.gethostbyname(url)
    c.connect((ip, 80))
    print '%s connected' % url
    c.sendall('GET /\r\n\r\n')
    return c.recv(1024)

urls = ['www.google.com', 'www.baidu.com', 'www.python.org']
pile = eventlet.GreenPile()
for x in urls:
    pile.spawn(geturl, x)

# note that the pile acts as a collection of return values from the functions
# if any exceptions are raised by the function they'll get raised here
for url, result in zip(urls, pile):
    print '%s: %s' % (url, repr(result)[:50])
