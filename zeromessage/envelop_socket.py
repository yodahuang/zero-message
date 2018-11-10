import asyncio
import zmq
import zmq.asyncio
import pickle

class EnvelopSocket:
    """A Wrapper around zeroMQ socket so that it uses pub-sub envelope.

    The serialization is done using pickle.
    """

    @classmethod
    def as_publisher(cls, port=5566):
        """Convenient factory method for getting a publisher
        
        Keyword Arguments:
            port {int} -- Binding port number (default: 5566)
        
        Returns:
            EnvelopSocket -- The generated wrapped socket
        """
        if not hasattr(cls, 'context'):
            cls.context = zmq.Context()
        publisher = cls.context.socket(zmq.PUB)
        publisher.bind("tcp://*:{}".format(port))
        return cls(publisher)
    
    
    @classmethod
    def as_subscriber(cls, ip='localhost', port=5566):
        """Convenient factory method for getting a subscriber

        Keyword Arguments:
            port {int} -- Connecting port number (default: 5566)

        Returns:
            EnvelopSocket -- The generated wrapped socket
        """
        if not hasattr(cls, 'context'):
            cls.context = zmq.asyncio.Context()
        subscriber = cls.context.socket(zmq.SUB)
        subscriber.connect("tcp://{}:{}".format(ip, port))
        return cls(subscriber)

    def __init__(self, socket):
        self.socket_ = socket
        self.subscribed = False

    def publish(self, topic, message):
        """Publish message on a topic.
        
        Arguments:
            topic {str} -- Topic name
            message {obj} -- A python object
        """
        self.socket_.send_multipart([topic.encode('utf-8'), pickle.dumps(message)])

    def subscribe(self, topic, callback, with_topic=False):
        """Subscribe to a topic. Note you need to handle the coroutine yourself
        
        Arguments:
            topic {str} -- Topic name
            callback {function} -- The callback function when received the message. 
                The message is passed in as the first argument normally.
                If setting with_topic to be True, then the callback accepts topic as the first argument and message the second.

        Keyword Arguments:
            with_topic {bool} -- Whether callback accepts topic name or not (default: False)

        Returns:
            [coroutine] -- [The subscribe coroutine]
        """
        assert not self.subscribed  # The subscribe method can be called only once
        self.subscribed = True
        self.socket_.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
        @asyncio.coroutine
        def receive_and_callback():
            while True:
                [received_topic, message] = yield from self.socket_.recv_multipart()
                message = pickle.loads(message)
                # Note here the callback is still blocking
                if not with_topic:
                    callback(message)
                else:
                    received_topic = received_topic.decode('utf-8')
                    callback(received_topic, message)

        return receive_and_callback

        



