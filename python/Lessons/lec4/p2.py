import pickle
import sys
import os


def get_path():
    return os.path.abspath(__file__)


if __name__ == "__main__":
    params = pickle.loads(sys.stdin.buffer.read())
    # print(params)
    print('{} the cat'.format(params[0]))
