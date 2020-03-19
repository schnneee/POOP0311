class SimpleMeta(type):
    def __new__(cls, classname, superclasses, attributedict):
        print("[new]class name:", classname)
        print("[new]parent class name:", superclasses)
        print("[new]attribute:", attributedict)
        return type.__new__(cls, classname, superclasses, attributedict)


class S:
    def __init__(self, name, age):
        print("[init] for S initialized")
        self.name = name
        self.age = age


class A(S, metaclass=SimpleMeta):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("[init] for A customize")

    pass


a1 = A("scott", 9)
print("a1 created successfully")