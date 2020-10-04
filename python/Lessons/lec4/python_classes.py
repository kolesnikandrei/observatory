import time


class Rec:
    pass


Rec.name = "Alice"
print(Rec.name)


a = Rec()
print(a.name)


def upper_name(self):
    return self.name.upper()


Rec.method_upper_name = upper_name
print(a.method_upper_name())
# a.surname = "In wonderland"
# print(a.surname)
# print(Rec.surname)

# class Dog:
#     def __init__(self):
#         self.voice = 'bark bark'
#
#     def barking(this):
#         print(this.voice)
#
#     def nothing(self):
#         pass


# lessy = Dog()
# lessy.barking()
#
# VERY_MUCH_ITERATIONS = 10000000
# start = time.time()
#
# for i in range(VERY_MUCH_ITERATIONS):
#     lessy.nothing()
#
# diff = time.time() - start
# print(diff)
#
#
# start = time.time()
# temp_var = lessy.nothing
#
# for i in range(VERY_MUCH_ITERATIONS):
#     temp_var()
#
# diff = time.time() - start
# print(diff)

# class Selfless:
#     def __init__(self, data):
#         self.data = data
#
#     def selfless(arg1, arg2): # Простая функция в 3.0
#         return arg1 + arg2
#
#     def normal(self, arg1, arg2): # Ожидает получить экземпляр при вызове
#         return self.data + arg1 + arg2
#
# s = Selfless(2)
# print(s.normal(3, 4)) # Экземпляр передается автоматически
#
# print(Selfless.normal(s, 3, 4)) # Метод ожидает получить self:
# print(Selfless.selfless(3, 4))
#
# s.selfless(3, 4)
# Selfless.normal(3, 4)
