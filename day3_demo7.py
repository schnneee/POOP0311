a1 = True
a2 = False
print(a1 and a1, a1 or a2, a2 and a2, a2 or a2, not a1, not a2)

B = [True, False, None, 3.14, "Hello world", '打個中文', 500]

print("-- True and b ------------------")
# A and B 時，當A為true，B可為任何東西
for b in B:
    print(a1 and b)

print("-- False and b ------------------")
# A and B 時，當A為false，B不管是啥都為false
for b in B:
    print(a2 and b)

print("-- True or b ------------------")
# A or B 時，當A為true，B不管是啥都為true
for b in B:
    print(a1 or b)

print("-- False or b ------------------")
# A or B 時，當A為false，A會是B
for b in B:
    print(a2 or b)