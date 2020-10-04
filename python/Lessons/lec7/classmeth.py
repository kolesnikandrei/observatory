class Spam:
    num_instances = 0                         # Use static method for class data

    def __init__(self):
        Spam.num_instances += 1

    def print_num_instances(cls):
        print("Number of instances: %s, %s" % (cls.num_instances, cls))
    print_num_instances = classmethod(print_num_instances)


class Sub(Spam):
    def print_num_instances(cls):                 # Override a static method
        print("Extra stuff...")              # But call back to original
        Spam.print_num_instances()
    print_num_instances = classmethod(print_num_instances)


class Other(Spam):
    pass


s = Sub()
s1 = Spam()
Sub.print_num_instances()
# s.printNumInstances()
s1.print_num_instances()
z = Other()
z.print_num_instances()
