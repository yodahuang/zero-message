import asyncio
import zmq
import zmq.asyncio
from zero_message import EnvelopSocket

port = "5556"
context = zmq.asyncio.Context()
socket = EnvelopSocket.as_subscriber(context, port)

def doSomething(msg):
    print(msg)

subscribe_coroutine = socket.subscribe('test', doSomething)

asyncio.get_event_loop().run_until_complete(subscribe_coroutine())