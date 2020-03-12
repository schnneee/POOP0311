v1 = []
v2 = ['Hello']
v3 = ()
v4 = ('Hello')
v5 = ('Hello',)
v6 = ('Hello', 'World')
print(type(v1), type(v2), type(v3), type(v4), type(v5), type(v6))
v7 = ('China', 'Italy', 'Korea', 'Iran')
print([v for v in v7])
print(v7[0], v7[3], v7[2])
print(hex(id(v7)))
# v7.append('US')
v7 += ('US',)
print(v7)
print(hex(id(v7)))

x1 = 5
x2 = 7
print(x1, x2)
x = x1
x1 = x2
x2 = x
print(x1, x2)

# 可輕易做值的交換
x3 = 5
x4 = 7
print(x3, x4, hex(id(x3)), hex(id(x4))) # 交換為指標交換
x3, x4 = x4, x3
print(x3, x4, hex(id(x3)), hex(id(x4)))

x5 = 'hello world'
x6 = 3.14
print(x5, x6, hex(id(x5)), hex(id(x6)))
x5, x6 = x6, x5
print(x5, x6, hex(id(x5)), hex(id(x6)))

p1 = 'A'
p2 = 'K'
p3 = 'Q'
p4 = 'J'
p5 = '10'
print(p1, p2, p3, p4, p5)
p5, p1, p3, p4, p2 = p1, p2, p3, p4, p5
print(p1, p2, p3, p4, p5)