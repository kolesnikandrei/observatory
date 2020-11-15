class A:

    def first_method(self):
        return 'first'

    def second_method(self):
        return 'second'


class B(A):
    def second_method(self):
        return 'reloaded second'

    def third_method(self):
        return 'third meth'


b: A = B()
print(b.first_method())
print(b.second_method())
print(b.third_method())
