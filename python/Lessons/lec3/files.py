# my_file = open('float_vs_decimal.py')
#
# try:
#     for line in my_file:
#         print(line)
# finally:
#     my_file.close()


# with open('float_vs_decimal.py', 'r') as f:
#     string = f.readlines()
#     print(string)


# def read_in_chunks(file_obj, chunk_size=2048):
#     """
#     Lazy function to read a file piece by piece.
#     Default chunk size: 2kB.
#
#     """
#     while True:
#         data = file_obj.read(chunk_size)
#         if not data:
#             break
#         yield data
#
#
# f = open('float_vs_decimal.py')
# for chunk in read_in_chunks(f):
#     print(chunk)
# f.close()


import fileinput

for line in fileinput.input(['float_vs_decimal.py']):
    print(line)

import sys
print(sys.getdefaultencoding())





