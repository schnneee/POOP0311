from collections import UserDict


class MyOwnDict(UserDict):
    def __init__(self, data={}, **kwargs):
        super().__init__()
        self.update(data)
        self.update(kwargs)

    def __add__(self, other):
        self.data.update(other)
        return self


a = MyOwnDict(a=1)
b = MyOwnDict(b=2)
c = MyOwnDict(c=567)
d = MyOwnDict(d={'a': 777})
print(type(a), type(b), type(c), type(d))
print(a.data, b.data, c.data, d.data)
print(a + b)
print(a + b + c)
print(a + b + c + d)