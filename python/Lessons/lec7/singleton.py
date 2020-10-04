# 3.X and 2.X: classes

class singleton:
    def __init__(self, aClass):  # On @ decoration
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):  # On instance creation
        if self.instance is None:
            self.instance = self.aClass(*args, **kwargs)  # One instance per class
        return self.instance


##################################################################################

# test code


@singleton  # Person = singleton(Person)
class Person:  # Rebinds Person to onCall
    def __init__(self, name, hours, rate):  # onCall remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton  # Spam = singleton(Spam)
class Spam:  # Rebinds Spam to onCall
    def __init__(self, val):  # onCall remembers Spam
        self.attr = val


bob = Person('Bob', 40, 10)  # Really calls onCall
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)  # Same, single object
print(sue.name, sue.pay())

X = Spam(val=42)  # One Person, one Spam
Y = Spam(99)
print(X.attr, Y.attr)
