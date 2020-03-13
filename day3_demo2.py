s1 = {'A', 'P', 'P', 'L', 'E'}
s2 = set(list("APPLE")) # 集合結果為無序 (因使用binary tree)
print(type(s1), type(s2), s1, s2, len(s1), len(s2))
print(s1 == s2)
print(s1 < s2, s1 > s2) # < > 非大小，是包含於的意思
s3 = {'E', 'A', 'P', 'L', 'X'}
print(s1 < s3, s1 > s3)
print('E' in s1, 'e' in s1)
s1.add('Z')
print(s1)
s1.remove('A')
print(s1)
# will crash
# s1.remove('A')
s4 = set(list('BANANA'))
print(s2, s4)
print("intersection:", s2 & s4) # 交集
print("union:", s2 | s4) # 聯集
print("xor union:", s2 ^ s4) # 互斥聯集
print("manual calculate xor:", (s2 | s4) - (s2 & s4))
print("equal?", (s2 ^ s4) == ((s2 | s4) - (s2 & s4)))