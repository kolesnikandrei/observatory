# Пункт 1: слоты в подклассе, но не в суперклассе

class C:
    pass


class D(C):
    __slots__ = ['а']  # Создает словарь экземпляра для неслотовых имен


d = D()
d.a = 1
d.b = 2

print(d.__dict__)
print(D.__dict__.keys())
print('-' * 40)


class C:
    __slots__ = ['а']


class D(C):
    pass


d = D()
# Но
d.a = 1
d.b = 2
print(d.__dict__)
print(C.__dict__.keys())
print('-' * 40)


class C:
    __slots__ = ['a']  # Пункт 3: доступен только самый нижний слот


class D(C):
    __slots__ = ['а']



d = D()
# Но
d.a = 1
# d.b = 2
# print(d.__dict__)
print(C.__dict__.keys())
print(D.__dict__.keys())
print('-' * 40)


# class C:
#     __slots__ = ['a']
#     a = 40
