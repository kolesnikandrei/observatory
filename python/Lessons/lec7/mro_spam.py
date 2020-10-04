# class A:
#     def spam(self):
#         print('A.spam')
#         super().spam()
#
#
# class B:
#     def spam(self):
#         print("B.spam")
#
#
# class C(A, B):
#         pass
#
#
# c = C()
# c.spam()
# print(C.__mro__)
#

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        print('A.__init__1')
        super().__init__()
        print('A.__init__2')

class B(Base):
    def __init__(self):
        print('B.__init__1')
        super().__init__()
        print('B.__init__2')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

c = C()
Base.__init__
B.__init__
A.__init__
C.__init__
print(C.__mro__)