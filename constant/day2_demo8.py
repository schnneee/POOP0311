x = 5
print(type(x), x, hex(id(x)))
x = 6
print(type(x), x, hex(id(x)))
y = 5
print(type(y), y, hex(id(y)))
y = 6
print(type(y), y, hex(id(y)))
z = [5]
print(type(z), z, hex(id(z)), hex(id(z[0])))
z[0] = 6
print(type(z), z, hex(id(z)), hex(id(z[0])))