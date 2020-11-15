import unittest
# ---------------------------------------------------------------------------------------------------------------
def font(tag):

    def decorate(func):
        def on_call(*args, **kws):
            return f"<{tag}>{func(*args, **kws)}</{tag}>"
        return on_call
    return decorate


@font('i')
@font('b')
def f1(): return "text"


print(f"decorated function:{f1()}")

# ---------------------------------------------------------------------------------------------------------------


def font(tag):

    def decorate(cls):

        class Wrapper:
            def __init__(self, *args):
                self.wrapped = cls(*args)

            def __getattr__(self, item):
                if item == "text":
                    return f"<{tag}>{getattr(self.wrapped, item)}</{tag}>"
                return getattr(self.wrapped, item)

        return Wrapper

    return decorate


@font('i')
@font('b')
class C1:
    def __init__(self, text):
        self.text = text


c1 = C1("text")
print(f"decorated class instance:{c1.text}")
c1 = C1("abra-cadabra")
print(f"decorated class instance:{c1.text}")
