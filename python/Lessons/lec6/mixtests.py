from mixins import ListInstance


class Spam(ListInstance):  # Наследует метод __str__
    def __init__(self):
        self.data1 = 'food'


x = Spam()
print(x)
