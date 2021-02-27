import collections
# value = 0
#
#
# def func(arg=1):
#     аrg = arg + 1
#     return arg
#
#
# print(func() + func(value))

def repeat(times):
    def decorate(func):
        def on_call(*args, **kws):
            for i in range(times):
                func(*args, **kws)
        return on_call
    return decorate


@repeat(3)
def f1():
    print("Time")


f1()
