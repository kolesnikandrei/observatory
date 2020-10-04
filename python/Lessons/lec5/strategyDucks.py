print('------------------------1---------------------------')

class Duck:

    def quack(self):
        print('quack')

    def swim(self):
        print('I\'m float')

    def display(self):
        pass

    def fly(self):
        print('I\'m flying')


class MallardDuck(Duck):
    def display(self):
        print('I\'m a mallard duck')


class RedHeadDuck(Duck):
    def display(self):
        print('I\'m a redhead duck')


print('------------------------2---------------------------')


class RubberDuck(Duck):
    def display(self):
        print('It seems like rubber DUCK')

    def quack(self):
        print('squuueeeck')

    #переопределять ли fly?


class DecoyDuck(Duck):
    def display(self):
        print('It seems like decoy DUCK')
