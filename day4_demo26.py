class SingletonParent(object):
    _instance = None

    def __init__(self):
        print("init is called")

    def __new__(cls, *args, **kwargs): # 有用到記憶體配置才用new
        print("new is called")
        if not cls._instance:
            print("object really created")
            cls._instance = object.__new__(cls, *args, **kwargs)
        print('return instance')
        return cls._instance


class A(SingletonParent):
    pass


class B:
    pass


print("start from a1")
a1 = A()
print("\nstart from a2")
a2 = A()
b1 = B()
b2 = B()

print(hex(id(a1)))
print(hex(id(a2)))
print(a1 == a2)
print(hex(id(b1)))
print(hex(id(b2)))
print(b1 == b2)