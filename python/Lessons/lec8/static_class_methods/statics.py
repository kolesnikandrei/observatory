class Spam:
    num_instances = 0                         # Use static method for class data

    def __init__(self):
        Spam.num_instances += 1

    def print_num_instances():
        print("Number of instances: %s" % Spam.num_instances)
    print_num_instances = staticmethod(print_num_instances)


class Sub(Spam):
    def print_num_instances():                 # Override a static method
        print("Extra stuff...")              # But call back to original
        Spam.print_num_instances()
    print_num_instances = staticmethod(print_num_instances)


s = Sub()
s1 = Spam()
a = Spam()
print("--------{}".format(a.num_instances))
Sub.print_num_instances()
s.print_num_instances()
Spam.print_num_instances()
