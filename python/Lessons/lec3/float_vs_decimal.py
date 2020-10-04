
print(round(3.45, 1))
print(round(3.55, 1))

print("%0.30f" % 3.45)
print("%0.30f" % 3.55)
print("-------------------")

# ---------1-2-3-4-5-6-7-8-9----------------

print(round(1.5))
print(round(2.5))
print(round(3.55))
print(round(4.5))

print("%0.30f" % 1.5)
print("%0.30f" % 2.5)
print("%0.30f" % 3.55)
print("%0.30f" % 4.5)

print("-------------------")
# --------------------------------------------

print(round(3.55, 1))
print(round(3.65, 1))
print(round(3.651, 1))
print(round(3.75, 1))
print(round(3.85, 1))
print("-------------------")

print("%0.30f" % 3.55)
print("%0.30f" % 3.65)
print("%0.30f" % 3.651)
print("%0.30f" % 3.75)
print("%0.30f" % 3.85)
print("-------------------")
# --------------------------------------------

from decimal import *
getcontext().prec = 6
print(Decimal(1) / Decimal(7))
print(Decimal('0.142857'))
getcontext().prec = 28
print(Decimal(1) / Decimal(7))
print(Decimal('0.1428571428571428571428571429'))

from decimal import *
print(getcontext())
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])
