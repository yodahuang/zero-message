import time
from zero_message import EnvelopSocket

socket = EnvelopSocket.as_publisher()

while True:
    socket.publish('test', {
        'data': [1, 2, 3]
    })
    time.sleep(1)