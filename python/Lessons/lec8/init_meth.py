
class A:
    def __enter__(self):
        print('enter A')

    def __exit__(self, ex_t, ex_v, trace):
        print('exit A')


class B:
    def __enter__(self):
        print('enter B')

    def __exit__(self, ex_t, ex_v, trace):
        print('exit B')


class Example:
    def __init__(self, param):
        with A() as a, B() as b:
            self.a, self.b, self.c = a, b, param


e = Example('c_param')
print(e.c)


print('----------------1-----------------------')
from contextlib import contextmanager, ContextDecorator


@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    try:
        resource = open('resource.txt', args[0])
        yield resource
    finally:
        # Code to release resource, e.g.:
        resource.close()


with managed_resource('w') as resource:
     resource.write('test')

print('----------------2-----------------------')


class my_context(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False


@my_context()
def my_function():
    print('The bit in the middle')


my_function()


with my_context():
    print('The bit in the middle')

# def f():
#     with cm():
#         # Do stuff
# @cm()
# def f():
#     # Do stuff
