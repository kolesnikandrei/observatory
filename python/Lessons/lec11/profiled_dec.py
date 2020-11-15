import time


def stats(name):
    """Decorator for send stats to graphite"""

    def _timing(func):
        def _wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = (time.time() - start) * 1000  # msec
            message = '%s %d %d\n' % (name, duration, time.time())

            print(message)

            # import socket
            # sock = socket.socket()
            # sock.connect((CARBON_SERVER, CARBON_PORT))
            # sock.sendall(message)
            # sock.close()

            return result

        return _wrapper

    return _timing
