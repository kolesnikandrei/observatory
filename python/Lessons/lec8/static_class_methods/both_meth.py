
class Methods:
    def i_meth(self, x):            # Normal instance method: passed a self
        print([self, x])

    def s_meth(x):                  # Static: no instance passed
        print([x])

    def c_meth(cls, x):             # Class: gets class, not instance
        print([cls, x])

    s_meth = staticmethod(s_meth)    # Make smeth a static method (or @: ahead)
    c_meth = classmethod(c_meth)     # Make cmeth a class method (or @: ahead)


m = Methods()
Methods.i_meth(m, 10)
Methods.s_meth(10)
Methods.c_meth(10)
print("--------------")
m.i_meth(10)
m.s_meth(10)
m.c_meth(10)
