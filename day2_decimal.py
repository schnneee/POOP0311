from decimal import Decimal

x1 = Decimal(100)
x2 = Decimal(200)
print(x1 + x2)
x3 = Decimal(2.968)
print(x3)
x4 = Decimal('2.968')
print(x4)
x5 = Decimal(2.968)
x6 = Decimal(2968)*Decimal(0.001)
print(x5-x6)
x7 = Decimal(2968)*Decimal('0.001')
print(x5-x7)
x8 = Decimal('2.968')-Decimal(2968)*Decimal('0.001')
print(x8)