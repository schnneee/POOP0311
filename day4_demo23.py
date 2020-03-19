class SimpleMeta(type): # metaclass => class 的 class
    def __new__(cls, classname, superclasses, attributedict):
        print("[new]class name:", classname)
        print("[new]parent class name:", superclasses)
        print("[new]attribute:", attributedict)
        return type.__new__(cls, classname, superclasses, attributedict)


class A(object, metaclass=SimpleMeta):
    def __init__(self):
        print("[init] for A customize")
    pass


a1 = A()
print("a1 created successfully")