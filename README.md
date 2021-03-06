## Zero Message

[![Documentation Status](https://readthedocs.org/projects/zero-message/badge/?version=latest)](https://zero-message.readthedocs.io/en/latest/?badge=latest)



*Zero Message* is a lightweight ROS-like pub-sub tool for Python 3.4+.

- Provides a wrapper around [ZeroMQ](http://zeromq.org) socket.
- Communicate between any Python program using publisher-subscriber protocol

### Installation

You need `zeromq` installed on your system. Refer to the [official guide](http://zeromq.org/intro:get-the-software).  For your convenience, here's some common ones:
```
# Debian-based
sudo apt-get install libzmq3-dev

# RHEL-based
sudo yum install libzmq3-devel

# Mac
brew install zmq
```

Then you can install this library

```
pip install zeromessage
```

### Quick start

Refer to the `/examples`:

```python
# listener.py
import asyncio
from zeromessage import EnvelopSocket

socket = EnvelopSocket.as_subscriber()

def doSomething(msg):
    print(msg)

subscribe_coroutine = socket.subscribe('test', doSomething)

asyncio.get_event_loop().run_until_complete(subscribe_coroutine())
```

```python
# talker.py
import time
from zeromessage import EnvelopSocket

socket = EnvelopSocket.as_publisher()

while True:
    socket.publish('test', {
        'data': [1, 2, 3]
    })
    time.sleep(1)
```

### Command Line tools

A `rostopic` like tool is provided.

```
zerotopic echo -- --help
```

### API Document

The document is currently broken. In the mean time you can just take a look at the well-documented source code.

[zero-message.readthedocs.io](http://zero-message.readthedocs.io)
