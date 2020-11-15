from dataclasses import dataclass, field
from typing import List


class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# -------------------------------------------------------
@dataclass
class Book:
    title: str
    author: str


book = Book(title="Fahrenheit 451", author="Bradbury")
other = Book("Fahrenheit 451", "Bradbury")
print(book)
print(other)
print(book == other)

print('-------------------------------')

tup = ('hello', object(), 42)
print(tup[0])
print(tup[1])
print(tup[2])

print('--------------------------------')

from collections import namedtuple


Car = namedtuple('Car', 'color mileage')
Car_2 = namedtuple('Audi', ['color', 'mileage'])

car = Car('black', 15000)
car_2 = Car_2('yellow', 10000)

print(car, car_2)
print(*car)
color, mileage = car_2
print(color, mileage)
print(car_2.color, car_2.mileage)
print(car_2[0], car_2[1])
print(car)

# car.color = "red"
print('--------------------------------')


class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
             return '#ff0000'
        else:
             return '#000000'


car = MyCarWithMethods("red", 10000)
print(car.hexcolor())

print('----------------------------------')

print(car._asdict())
print(car._replace(color="green"))
print(Car._make(["white", 150000]))

print('----------------------------------')

NamedTupleBook = namedtuple("NamedTupleBook", ["title", "author"])
book = NamedTupleBook('green', 10000)
car = Car('green', 10000)
print(car == book)

print('----------------------------------')

from dataclasses import make_dataclass
Book = make_dataclass("Book", ["title", "author"])
book = Book("Fahrenheit 451", "Bradbury")


@dataclass
class Book:
    title: str = "Unknown"
    author: str = "Unknown author"


print(Book())
print(Book("Farenheit 451"))


@dataclass(frozen=True)
class Book:
    title: str
    author: str


book = Book("Fahrenheit 451", "Bradbury")
# book.title = "1984"


# @dataclass
# class Bookshelf:
#     books: List[Book] = []

@dataclass
class Bookshelf:
    books: List[Book] = field(default_factory=list)


@dataclass
class Book:
    title: str
    author: str
    desc: str = None

    def __post_init__(self):
        self.desc = self.desc or "`%s` by %s" % (self.title, self.author)


print(Book("Fareneheit 481", "Bradbury"))
