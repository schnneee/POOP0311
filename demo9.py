print(round(1.0), round(1.1), round(1.4), round(1.5), round(1.6), round(1.9))
print(round(2.0), round(2.1), round(2.4), round(2.5), round(2.6), round(2.9))
print(round(3.0), round(3.1), round(3.4), round(3.5), round(3.6), round(3.9))


print(round(1.5), round(2.5), round(3.5), round(4.5), round(5.5))
print(round(13579.5), round(2468.5), round(1357.4), round(2468.6))

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN

value1 = Decimal(1.5)
value2 = Decimal(2.5)
value3 = Decimal(3.5)
output1 = Decimal(value1.quantize(1, rounding=ROUND_HALF_UP))
output2 = Decimal(value2.quantize(1, rounding=ROUND_HALF_UP))
output3 = Decimal(value3.quantize(1, rounding=ROUND_HALF_UP))
print(output1, output2, output3)
output1 = Decimal(value1.quantize(1, rounding=ROUND_HALF_DOWN))
output2 = Decimal(value2.quantize(1, rounding=ROUND_HALF_DOWN))
output3 = Decimal(value3.quantize(1, rounding=ROUND_HALF_DOWN))
print(output1, output2, output3)
output1 = Decimal(value1.quantize(1, rounding=ROUND_HALF_EVEN))
output2 = Decimal(value2.quantize(1, rounding=ROUND_HALF_EVEN))
output3 = Decimal(value3.quantize(1, rounding=ROUND_HALF_EVEN))
print(output1, output2, output3)

# 複數
x1 = 5 + 3j
x2 = 4 - 6j
print(type(x1), type(x2))
print(x1+x2, x1-x2, x1*x2, x1/x2)
print(x1.conjugate(), x2.conjugate())
print(abs(x1), 34**0.5)
print(type(-1),type((-1)**0.5), (-1)**0.5)
