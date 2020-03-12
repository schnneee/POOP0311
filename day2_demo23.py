import copy

l1 = list('abcdefg')
l2 = l1
l3 = list(l1)
l4 = l1[:]
l5 = copy.copy(l1)
l6 = copy.deepcopy(l1)
print(l1, l2, l3, l4, l5, l6)
print("l1", hex(id(l1)))
print("l2", hex(id(l2)))
print("l3", hex(id(l3)))
print("l4", hex(id(l4)))
print("l5", hex(id(l5)))
print("l6", hex(id(l6)))
l1[0] = 'A'
l2[1] = 'B'
l3[2] = 'C'
l4[3] = 'D'
l5[4] = 'E'
l6[5] = 'F'
print(l1, l2, l3, l4, l5, l6)
