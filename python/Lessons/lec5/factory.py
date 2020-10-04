def factory(aClass, *args):  # Кортеж с переменным числом аргументов
    return aClass(*args)  # Вызов aClass (или apply, только в 2.6)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job


object1 = factory(Spam)  # Создать объект Spam
object2 = factory(Person, "Guido", "guru")  # Создать объект Person

object1.doit('VanRossum')
print(object2.name)
