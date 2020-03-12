l1 = list('ABCDEF')
print('d' in l1, 'D' not in l1)
l2 = ['Apple', 'Banana', 'Cirtron']
print('Apple' in l2, 'A' in l2)
l3 = [l1, l2]
print(l3)
l3.append('Kiwi')
print(l3)
print('Banana in:', l2.index('Banana'))
#print('banana in:', l2.index('banana'))
p = 'Banana'
if p in l2:
    print('found, index=', l2.index(p))
else:
    print('not found')
print(l3.count('Kiwi'))
l4 = list('ABBAAABBBBBAADDDCCCCAABABABABA')
print(l4.count('A'), l4.count('B'))