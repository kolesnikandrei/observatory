# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):

    def __init__(self, speed):
        self._speed = speed

    def hit_and_run(self):
        """
        Шаблонный метод
        """
        self._move('вперед')
        self._stop()
        self._attack()
        self._move('назад')

    @abstractmethod
    def _attack(self):
        pass

    @abstractmethod
    def _stop(self):
        pass

    def _move(self, direction):
        """
        Передвижение - у всех отрядов одинаковое, в шаблон не входит

        :param direction: направление движения
        """
        self._output('движется {} со скоростью {}'.format(direction, self._speed))

    def _output(self, message):
        print('Отряд типа {} {}'.format(self.__class__.__name__, message))


class Archers(Unit):

    def _attack(self):
        self._output('обстреливает врага')

    def _stop(self):
        self._output('останавливается в 100 шагах от врага')


class CavaleryMen(Unit):

    def _attack(self):
        self._output('на полном скаку врезается во вражеский строй')

    def _stop(self):
        self._output('летит вперед, не останавливаясь')


if __name__ == '__main__':
    archers = Archers(4)
    archers.hit_and_run()
    cavalery_men = CavaleryMen(8)
    cavalery_men.hit_and_run()
