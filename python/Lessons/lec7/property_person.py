class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return f"My name is {self._first_name}"

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can\'t do that')


p = Person("Guido")
print(p.first_name)
try:
    p.first_name = 47
except TypeError as e:
    print(f'Error was: {e}')
try:
    del p.first_name
except AttributeError as e:
    print(f'Error was: {e}')


print(Person.first_name.fdel, Person.first_name.fget, Person.first_name.fset)
print(dir(Person.first_name))

