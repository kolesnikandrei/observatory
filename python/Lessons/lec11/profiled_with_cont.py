
import time

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003


class Stats(object):
    """Context manager for send stats to graphite"""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        duration = (time.time() - self.start) * 1000  # msec
        message = '%s %d %d\n' % (self.name, duration, time.time())

        print(message)

        # import socket
        # sock = socket.socket()
        # sock.connect((CARBON_SERVER, CARBON_PORT))
        # sock.sendall(message)
        # sock.close()
