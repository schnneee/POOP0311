s1 = set(list('APPLE'))
print(s1)
s1.add(3.14)
s1.add("Hello world")
s1.add(500)
s1.add(True)
s1.add(None)
print(s1)
print(None in s1)
# 因為是弱型別所以可以塞任何東西
s2 = set(list('BANANA'))
s1.add(s2) # 不可直接加入集合，會噴exception