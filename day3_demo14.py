x = range(10)
print(type(x), x, list(x))
x1 = range(5, 10) # 包頭不包尾
print(len(x1), list(x1))
x1 = range(-5, 5)
print(list(x1))
x2 = range(5, -5)
print("pos==>negative", list(x2))
x3 = range(0, 10, 2)
print(list(x3))
from numpy import arange
from numpy import linspace

y1 = arange(10)
print(type(y1), y1)
y1 = arange(5, 10)
print(type(y1), y1)
y2 = arange(0, 1, 0.05) # 可支援小數點的range
print(type(y2), y2)
z1 = linspace(0, 10)  # 切割 num預設50
print(type(z1), len(z1), z1)
z2 = linspace(0, 10, 10) # 切成10個
print(type(z2), len(z2), z2)
z3 = linspace(0, 10, 11) # 切成11個
print(type(z3), len(z3), z3)