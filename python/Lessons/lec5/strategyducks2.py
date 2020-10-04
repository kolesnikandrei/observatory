
class Duck:

    def swim(self):
        print('im float')

    def display(self):
        pass


class Quackble:

    def quack(self):
        print('quack')


class Flyable:

    def fly(self):
        print('Im flying')


class MallardDuck(Duck, Quackble, Flyable):
    def display(self):
        print('IM A MALLARD DUCK')


class RedHeadDuck(Duck, Quackble, Flyable):
    def display(self):
        print('IM A RedHead DUCK')


class RubberDuck(Duck, Quackble):
    def display(self):
        print('It seems like rubber DUCK')

    def quack(self):
        print('squuueeeck')


class DecoyDuck(Duck):
    def display(self):
        print('It seems like decoy DUCK')


