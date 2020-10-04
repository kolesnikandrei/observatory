
def tracer(func):                      # Remember original
    print(func)

    def on_call(*args):                 # On later calls
        print(args)
        on_call.calls += 1
        print('call %s to %s' % (on_call.calls, func.__name__))
        return func(*args)
    print("1")
    on_call.calls = 0
    return on_call


class C:
    @tracer
    def spam(self, a, b, c): return a + b + c


# x = C()
# print("---------------------")
# print(x.spam(1, 2, 3))
# print("---------------------")
# print(x.spam('a', 'b', 'c'))           # Same output as tracer1 (in tracer2.py)

@tracer                                # Same as spam = tracer(spam)
def spam(a, b, c):                     # Wrap spam in a decorator object
    return a + b + c


print(spam(1, 2, 3))                   # Really calls the tracer wrapper object
print(spam('a', 'b', 'c'))             # Invokes __call__ in class