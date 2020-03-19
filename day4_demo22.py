from abc import ABC, abstractmethod

class A1(ABC): #抽象
    def __init__(self,value):
        self.value = value
        super().__init__()
    @abstractmethod
    def do_something(self):
        pass

class B1(A1):
    def do_something(self):
        print('hello world[%d]'%self.value)

#a1 = A1(100)
#a1.do_something() =>exception 因為A1本身為抽象類別
b1 = B1(100)
b1.do_something()
print(type(A1), type(B1), type(b1))