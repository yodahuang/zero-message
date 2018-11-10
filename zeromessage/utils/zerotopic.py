import asyncio
import argparse

import zmq
import zmq.asyncio
import fire

from zeromessage import EnvelopSocket

def echo(topic, port=5566):
    socket = EnvelopSocket.as_subscriber(port=port)

    subscribe_coroutine = socket.subscribe(topic, lambda m_topic, message: print('{} | {}'.format(m_topic, message)), with_topic=True)
    asyncio.get_event_loop().run_until_complete(subscribe_coroutine())

def main():
    fire.Fire({
        'echo': echo
    })

if __name__ == '__main__':
    main()