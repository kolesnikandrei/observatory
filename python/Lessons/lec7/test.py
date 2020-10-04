# s = iter("qwerty")
# print(*s)
# for i in s:
#     pass
#
# next(s)
# print('-----------------------')
# print('-----------------------')
#
# li = [1, 2, 3]
#
# for i in li:
#     pass
# print(*li)
#
#
# my_iterator = zip([1, 2, 3, 4], [1, 2, 3, 4])
#
# my_list = [*my_iterator]
# print(my_list)

# print('-----------------------')
# print('-----------------------')
#
# tags = ['man', 'you', 'are', 'awesome']
# entries = [['man', 'that\'s'], ['right', 'awesome']]
# print([entry for tag in tags for entry in entries if tag in entry])
#
# print('-----------------------')
# print('-----------------------')
# a = {frozenset([1, 2, 3]): "value"}
# print(a)
# b = {}
# b1 = {(1, 2), (1, 2)}
# b2 = set((1,
#           "2",
#           "3",
#           ))
# b3 = {3}
# print(type(b))
# print(type(b1))
# print(type(b2))
# print(type(b3))
# print('-----------------------')
# print('-----------------------')


# class A:
#     n = 0
#
#     def __str__(self):
#         return str(self.n + 9)
#
#     def __repr__(self):
#         return str(self.n - 9/9)
#
#
# print([A()])

print('-----------------------')
print('-----------------------')

s = 'a0-b1-c2-d3-e4-f5-g6'
print(s[3:12:3])
print(s[::3])
print(s[2::3])
print(s[::-1])
