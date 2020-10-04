class Animal:
    def make_voice(self):
        pass


class Cat(Animal):
    def make_voice(self):
        print('meow')


class Dog(Animal):
    def make_voice(self):
        print('bark')


cat = Cat()
dog = Dog()
cat.make_voice()
dog.make_voice()

print('-------------------------------------1------------------------------------')


class Animal2:
    def make_voice(self):
        self.do_voice()


class Cat2(Animal2):
    def do_voice(self):
        print('meow')


class Dog2(Animal2):
    def do_voice(self):
        print('bark')


cat = Cat2()
dog = Dog2()
cat.make_voice()
dog.make_voice()

print('---------------------------------------2-------------------------------')


class Animal3:
    def make_voice(self):
        print(self)
        self.do_voice()


class Cat3(Animal3):
    def do_voice(self):
        print('meow')

    def __repr__(self):
        return 'Im a cat'


class Dog3(Animal3):
    def do_voice(self):
        print('bark')

    def __repr__(self):
        return 'Im a dog'


cat = Cat3()
dog = Dog3()
cat.make_voice()
dog.make_voice()
print('---------------------------------------3-------------------------------')
from abc import ABCMeta, abstractmethod


class Animal4(metaclass=ABCMeta):
    def makevoice(self):
        print(self)
        self.do_voice()

    @abstractmethod
    def do_voice(cls):
        pass


class Cat4(Animal4):
    def do_voice(self):
        print('meow')

    def __repr__(self):
        return 'Im a cat'


class Dog4(Animal4):
    def do_voice(self):
        print('bark')

    def __repr__(self):
        return 'Im a dog'


cat = Cat4()
dog = Dog4()
cat.makevoice()
dog.makevoice()
