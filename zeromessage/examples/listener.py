import asyncio
from zeromessage import EnvelopSocket

socket = EnvelopSocket.as_subscriber()

def doSomething(msg):
    print(msg)

subscribe_coroutine = socket.subscribe('test', doSomething)

asyncio.get_event_loop().run_until_complete(subscribe_coroutine())