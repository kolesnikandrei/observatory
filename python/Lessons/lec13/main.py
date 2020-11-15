import urllib.request
import time


def download_image(imagePath, fileName):
    print("Downloading Image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)


def main():
    for i in range(10):
        image_name = "temp/image-" + str(i) + ".jpg"
        download_image("http://lorempixel.com/400/200/sports", image_name)


if __name__ == '__main__':
    t0 = time.time()
    main()
    total_time = time.time() - t0
    print(f'total_time: {total_time}')
