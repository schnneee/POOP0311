a1 = 5
a2 = a1
print(a1, a2)
print(hex(id(a1)), hex(id(a2)))
a1 = 6
print(a1, a2)
print(hex(id(a1)), hex(id(a2)))
v1 = [5]
v2 = v1
# 記憶體位置相同
print(v1, v2)
print(hex(id(v1)), hex(id(v2)), hex(id(v1[0])), hex(id(v2[0])))
v1[0] = 6
print(v1, v2)
print(hex(id(v1)), hex(id(v2)), hex(id(v1[0])), hex(id(v2[0])))
