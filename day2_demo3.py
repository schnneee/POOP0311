x = 5
print(type(x))
x = [1,2,3]
print(type(x))

a1 = '500'
a2 = "3.14"
a3 = "True"
a4 = "False"
a5 = "3+7j"
b1 = int(a1)
print(b1, type(b1))
b2 = int(True)
print(b2, type(b2))
b3 = complex(-1)
print(b3, type(b3))

try:
    b4 = int(a3)  # 字串的True 轉不過去
    print(b4, type(b4))
except:
  print("An exception occurred")