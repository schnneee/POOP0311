class Course:
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    def __str__(self):
        return f'[{hex(id(self))}]course:{self.name}, instructor:{self.instructor}, duration:{self.duration}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.instructor == other.instructor and self.duration == other.duration
        # pass

    def __hash__(self):
        return hash((self.name, self.instructor, self.duration))


a1 = Course('BDPY', 'Mark', 35)
a2 = a1
a3 = Course('PYKT', 'Mark', 35)
a4 = Course('BDPY', 'Mark', 35)
print(a1)
print(a2)
print(a3)
print(a4)
print('a1 hash', hash(a1))
print('a2 hash', hash(a2))
print('a3 hash', hash(a3))
print('a4 hash', hash(a4))
print([a1, a2, a3])
s1 = set()
s1.add(a1)
print("[1]", s1)
s1.add(a2)
print("[2]", s1)
s1.add(a3)
print("[3]", s1)
s1.add(a4)
print("[4]", s1)