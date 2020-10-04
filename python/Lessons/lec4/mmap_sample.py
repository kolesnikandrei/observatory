import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    file_size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, file_size, access=access)


# create file
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')


m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])
m[0:11] = b'Hello World'
m.close()

with open('data', 'rb') as f:
    print(f.read(20))

# print('-----as context manager------')
# with memory_map('data') as m:
#     print(len(m))
#     print(m[0:11])
