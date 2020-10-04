def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, item):
            print('self: {}, item: {}'.format(self, item))
            return getattr(self.wrapped, item)

        # def __str__(self):
        #     return "Wrapper obj"
    return Wrapper


@decorator
class C:
    def __init__(self, x, y):
        self.attr = 'spam'


# x = C(6, 7)
# print(x.attr)


def bold(func):
    def on_call(*args):
        return f"<b>{func(*args)}</b>"
    return on_call


def italic(func):
    def on_call(*args):
        return f"<i>{func(*args)}</i>"
    return on_call

@italic
@bold
def f1(): return "text"


print(f1())


class C1:
    text = "text"


print(C1.text)