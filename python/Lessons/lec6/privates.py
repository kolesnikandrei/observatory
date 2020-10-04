
class A:
    def __init__(self):
        self.__internal = 0
        self.public = 1

    def public_method(self):
        pass

    def __private_method(self):
        pass


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.__private = 1

    def __private_method(self):
        pass


a = A()
b = B()

print(dir(a))
print(dir(b))
