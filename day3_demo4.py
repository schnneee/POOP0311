class Person:
    def __init__(self, name):
        self.name = name

    pass


p1 = Person("Mark")
s1 = set()
s1.add(p1)
print(s1)
p2 = p1
s1.add(p1)
s1.add(p1)
s1.add(p2)
print(s1)
p3 = Person("Mark")
s1.add(p3)
print('after add p3', s1)