l1 = list('ABCDE')
print(l1 + l1)
print(l1 * 3, 3 * l1)

del l1[2]
print(l1)

print("l1 id=%s" % (hex(id(l1))))
l1 *= 3
print("l1 id=%s, l1*3 id=%s" % (hex(id(l1)), hex(id(l1 * 3))))

list1 = list('ABCDE')
string1 = 'ABCDE'
print("[step1],list1 id=%s, string1 id=%s" % (hex(id(list1)), hex(id(string1))))
list1 = list1 + ['F']
string1 = string1 + 'F'
print(list1, string1)
print("[step1],list1 id=%s, string1 id=%s" % (hex(id(list1)), hex(id(string1))))
# + 會assign一個新的記憶體位置

list2 = list('ABCDE')
list3 = list(list2)
print("before", list2, list3, hex(id(list2)), hex(id(list3)))
list2.append('F')
list3.extend('F')
print("after", list2, list3, hex(id(list2)), hex(id(list3)))
# append，extend 仍使用相同記憶體位置

list4 = list('ABCDE')
list5 = list4[:]
list6 = list4[:]
print(list4, list5, list6)
list4.append(['F', 'G'])
list5.extend(['F', 'G'])
list6 += ['F', 'G']
print(list4, list5, list6)
# append 會直接把物件加在後面
# extend 會拉平後再加在後面