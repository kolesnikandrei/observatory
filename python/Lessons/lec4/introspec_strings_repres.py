class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'{self.x} and {self.y}'

    def __repr__(self):
        return f'X: {self.x}, Y: {self.y}'


if __name__ == '__main__':
    p = Pair(4, 5)
    print(p)
    print('{0!r}'.format(p))
    list_os_pairs = [p]
    print(list_os_pairs)
