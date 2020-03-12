string1 = 'abcdefg1234567'
list1 = list(string1)
print(string1[0], string1[5], string1[-1])
print(string1[-2:], string1[5:8], string1[-8:-2])
print('x' in string1, 'g' in string1, 'PQR' not in string1)
print(hex(id(string1)))
string1 = string1[:5]
print(hex(id(string1)))
list1[0] = '*' # 可置換
print(list1)
string1[0] = '*' # 字串是imutable，會跳exception
print(string1)