import gevent
from gevent import monkey
import urllib.request
from time import time

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
url = "http://lorempixel.com/400/200/sports"


def download_image(image_path, file_name):
    print("Downloading Image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)


def get_filename(i):
    return "temp/image-" + str(i) + ".jpg"


t1 = time()
tasks = [gevent.spawn(download_image, url, get_filename(i)) for i in range(10)]
gevent.joinall(tasks, timeout=12.0)
print("Sucessful: %s from %s" % (sum(1 if task.value else 0 for task in tasks), len(tasks)))
print(time() - t1)
