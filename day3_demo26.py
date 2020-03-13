x = "hello global world"
y = "Hi"
print(x)
print(y)


def foo():
    print("inside foo, x=", x)


foo()
print("again, x=", x)
print(y * 2, y)
y = y * 2
print(y)


def bar():
    #y = 0
    global y # 指定抓外部變數
    y = y * 2
    print("y=", y)

bar()
print("in the end, y=",y)