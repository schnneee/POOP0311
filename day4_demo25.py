class MetaSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        print('[MS] inside __call__')
        if self not in self._instances:
            print("[MS]self not found, shall create one")
            self._instances[self] = super().__call__(*args, **kwargs)
            print("[MS]object created and registered")
        print('return instance')
        return self._instances[self]

class A(metaclass=MetaSingleton):
    def __init__(self):
        print("[A]init")
    pass
class B:
    def __init__(self):
        print("[B]init")
    pass
b1 = B()
print(b1, hex(id(b1)))
b2 = B()
print(b2, hex(id(b2)))
a1 = A()
print(a1, hex(id(a1)))
a2 = A()
print(a2, hex(id(a2)))