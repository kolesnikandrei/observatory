#
#
# with open('somefile.txt', 'wt') as f:
#     print('Hello world', file=f)
#
# # with open('somefile.txt', 'xt') as f:   # xb
# #     print('Hello world', file=f)
#
# import os
# if not os.path.exists('somefile.txt'):
#     with open('somefile.txt', 'wt') as f:
#         f.write('hello')
# else:
#     print('File already exists!')
#
#
# with open('somefile.bin', 'wb') as f:
#     text = 'Hello World'
#     f.write(text.encode('utf-8'))
#
# with open('somefile.bin', 'rb') as f:
#     data = f.read()
#     text = data.decode('utf-8')
#
# print(text)

# import array
# numbers = array.array('i', [1, 2, 3, 4])
# with open('data.bin', 'wb') as f:
#     f.write(numbers)


import io
s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)
print(s.getvalue())

s = io.StringIO('Hello\nWorld\n')  #BytesIO
print(s.read(4))
print(s.read())
