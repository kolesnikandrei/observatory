class Spam:
    num_instances = dict()                         # Use static method for class data

    def __init__(self):
        cls = self.__class__
        if cls.__name__ in cls.num_instances:
            cls.num_instances[cls.__name__] += 1
        else:
            cls.num_instances[cls.__name__] = 1

    def print_num_instances(cls):
        print("Number of instances: %s, %s" % (cls.num_instances[cls.__name__], cls))
    print_num_instances = classmethod(print_num_instances)


class Sub(Spam):
    def print_num_instances(cls):                 # Override a static method
        print("Extra stuff...")              # But call back to original
        Spam.print_num_instances()
    print_num_instances = classmethod(print_num_instances)


class Other(Spam):
    pass


s = Sub()
s2 = Sub()
s1 = Spam()
s2 = Spam()
Sub.print_num_instances()
s.print_num_instances()
s1.print_num_instances()

z = Other()    #????????
z.print_num_instances()


