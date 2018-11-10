import zmq
import time
from zero_message import EnvelopSocket

port = "5556"
context = zmq.Context()
socket = EnvelopSocket.as_publisher(context, port)

while True:
    socket.publish('test', {
        'data': [1, 2, 3]
    })
    time.sleep(1)