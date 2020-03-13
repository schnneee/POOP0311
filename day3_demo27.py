class Holder:
    def __init__(self, value):
        self.value = value


x = 10
y = [10]
z = Holder(10)

print(x, y[0], z.value)


def doubleValue():
    global x # imuatable 的東西要存取外部變數要加global
    x *= 2
    y[0] = y[0] * 2
    z.value = z.value * 2
doubleValue()

print(x, y[0], z.value)


y = 500

def foo():
    y = "local"
    print("inside y, y=", y)

print(y)
foo()
print(y)

