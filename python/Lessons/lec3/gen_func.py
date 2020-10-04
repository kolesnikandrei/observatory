# def gen():
#     for item in range(10):
#         x_item = yield item
#         print(x_item)
#
#
# generator = gen()
# print(next(generator))
# print('---')
# print(generator.send(50))
# print('---')
# print(generator.send(500))
# print('---')
# print(next(generator))


#  TASK(simple):
# Write generator expression to generate collection like "PPP", "YYY", "TTT", "HHH", "OOO", "NNN"
# Write generator function to generate collection like "PPP", "YYY", "TTT", "HHH", "OOO", "NNN"

# g = list((x*3 for x in "PYTHON"))
# print(g)
#
# def task1():
#     for x in 'PYTHON':
#         yield x*3
#
#
# print(list(task1()))

# TASK(medium): Transpose with gen expressions and gen function, iterate by elements and write to list conversations.
matrix = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8]]

