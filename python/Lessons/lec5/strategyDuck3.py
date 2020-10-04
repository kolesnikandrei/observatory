
class Duck:

    def set_fly_behavior(self, flying):
        self.flying = flying

    def set_quack_behavior(self, quacking):
        self.quacking = quacking

    def fly(self):
        self.flying.fly()

    def quacking(self):
        self.quacking.quack()

    def swim(self):
        print('im float')

    def display(self):
        pass


class FlyBehavior:
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print('im fly with wings')


class FlyNoWay(FlyBehavior):
    def fly(self):
        print('im not flying')


class FlyRocket(FlyBehavior):
    def fly(self):
        print('im flying WITH ROCKET')


class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('quack')


class Squeeck(QuackBehavior):
    def quack(self):
        print('squeeck')


class MuteQuack():
    def quack(self):
        print('SILENCE')


class MallardDuck(Duck):
    def __init__(self):
        self.flying = FlyWithWings()
        self.quacking = QuackBehavior()

    def display(self):
        print('IM A MALLARD DUCK')


class RedHeadDuck(Duck):
    def display(self):
        print('IM A RedHead DUCK')


class RubberDuck(Duck):
    def display(self):
        print('It seems like rubber DUCK')


class DecoyDuck(Duck):
    def display(self):
        print('It seems like decoy DUCK')


m = MallardDuck()
m.fly()
m.display()

