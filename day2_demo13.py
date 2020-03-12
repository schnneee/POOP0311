list1 = list('ABCDEFG')
list2 = [1, 3, 5, 7, 9]
list3 = ['apple', 'banana', 'citron', 'kiwi', 'watermelon']
string1 = "ABCDEF如果打中文"
for l1 in list1:
    print("*", l1)
sum = 0
for l2 in list2:
    sum += l2
print("total=%d" % sum)

for l3 in list3:
    print("%s has length %d" % (l3, len(l3)))

for l4 in string1:
    print("[", l4, "]")

lengths = []
for l3 in list3:
    lengths.append(len(l3))
print(lengths)

# 等於上面
print([len(l3) for l3 in list3])