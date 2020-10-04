from mixins import *


class Super:
    def __init__(self):
        self.data1 = 'spam'  # Создать атрибуты экземпляра

    def ham(self):
        pass


class Sub(Super, ListInstance, ListInherited):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):  # Определить еще один метод
        pass


if __name__ == '__main__':
    X = Sub()
    print(X)
