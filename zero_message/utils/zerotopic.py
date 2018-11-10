import asyncio
import argparse

import zmq
import zmq.asyncio
import fire

from zero_message import EnvelopSocket

def echo(topic, port=5556):
    context = zmq.asyncio.Context()
    socket = EnvelopSocket.as_subscriber(context, port)

    subscribe_coroutine = socket.subscribe(topic, lambda m_topic, message: print('{} | {}'.format(m_topic, message)), with_topic=True)
    asyncio.get_event_loop().run_until_complete(subscribe_coroutine())

def main():
    fire.Fire({
        'echo': echo
    })

if __name__ == '__main__':
    main()