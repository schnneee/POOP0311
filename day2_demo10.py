x1 = []
x2 = ['hello']
x3 = ()
x4 = {}
x5 = {'hello'}
x6 = {'hello': 'world'}
x7 = set()
print(type(x2), type(x1), type(x3), type(x4), type(x5), type(x6), type(x7))
y1 = ['a', 'b', 'c']
y2 = list("abc")
print(y1, y2, hex(id(y1)), hex(id(y2)))
print(hex(id(y1[0])), hex(id(y2[0])))
print(len(y1), len(y2))
y3 = [1, 2, 'c', 'd', True, False, None, 'hello world']
print(y3[0], y3[2], y3[5], y3[len(y3)-1])
print(y3[int(1.5)])