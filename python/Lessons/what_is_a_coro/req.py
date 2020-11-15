from requests import get, Response
from loop2 import wait

URLS = ['http://www.google.com', 'http://www.yandex.ru']
SIZE = 100


def read(r: Response) -> bytes:
    data = b""
    for chunk in r.iter_content(SIZE):
        data += chunk
        yield
    return data


def fetch(url: str) -> str:
    with get(url, stream=True) as r:
        data = yield from read(r)
        return data.decode("utf-8")


def main():
    coros = [fetch(url) for url in URLS]
    results = wait(coros)
    for result in results:
        print(f'{results[:20]!r}')


main()
