x1 ='ABC'
x2 = "Merry X'mas,Merry X'mas,Merry X'mas,Merry X'mas"
x3 = 'Merry X\'mas,Merry X\'mas,Merry X\'mas,Merry X\'mas'
x4 = b'ABC'
print(type(x1), type(x4), len(x1), len(x4))
x5 = '使用中文'
print(x5)
#x6 = b'使用中文'
print(x1, x4)

a1 = '500'
a2 = "3.14"
a3 = "True"
a4 = "False"
a5 = "3+7j"
#a6 = "www.uuu.com.tw"
b1 = int(a1)
b2 = float(a2)
b3 = bool(a3)
b4 = bool(a4)
b5 = complex(a5)
#b6 = int(a6)
print(b1, b2, b3, b4, b5)
print(type(b1), type(b2), type(b3), type(b4), type(b5))
print('originally, x4=',type(x4))
y4 = x4.decode('utf8')
print(type(x4), type(y4))