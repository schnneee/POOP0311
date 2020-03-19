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
        pass

    def __hash__(self):
        pass


a1 = Course('BDPY', 'Mark', 35)
a2 = a1
a3 = Course('PYKT', 'Mark', 35)
print(a1)
print(a2)
print(a3)
print([a1, a2, a3])