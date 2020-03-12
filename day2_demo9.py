x1 = ['apple', 'banana', 'citron']
x2 = x1
x3 = list(x1) # 只複製了值
x4 = x1[:] # 只複製了值
print(hex(id(x1)), hex(id(x2)), hex(id(x3)), hex(id(x4)))
print(x1, x2, x3, x4)
x1.append('Kiwi')
print(x1, x2, x3, x4)