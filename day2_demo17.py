l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = l1[:]
l1.insert(0, '*')
print(l1)
l1.insert(5, '!')
print(l1)
l1.remove('*')
print(l1)
l1.remove('!')
print(l1)
# l1.remove('*') 找不到元素時會報excption，需用in先檢查
print(l1.pop(5), l1)
print(l1.pop(5), l1)

l2 = list('QWERTYUIOPASDFGHJKL')
l2.sort()
print(l2)
l3 = list('qwertyupasdfghjklQWERTYUIOPASDFGHJKL')
print(id(l3))
l3.sort(reverse=True)
print(id(l3))
l3 = l3[::-1]
print(id(l3))

l3.sort(key=str.lower)
print(l3)