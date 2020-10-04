
class Attr:
    def __getattr__(self, item):
        if item == 'age':
            return 26
        else:
            raise AttributeError


x = Attr()
print(x.age)
# print(x.name)

print('----------------------')


class PropSquare:
    def __init__(self, start):
        self.value = start

    def get_x(self):                         # On attr fetch
        return self.value ** 2

    def set_x(self, value):                  # On attr assign
        self.value = value
    x = property(get_x, set_x)                # No delete or docs


p = PropSquare(3)       # 2 instances of class with property
q = PropSquare(32)      # Each has different state information

print(p.x)              # 3 ** 2
p.x = 4
print(p.x)              # 4 ** 2
print(q.x)              # 32 ** 2 (1024)
