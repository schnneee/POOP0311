class Program:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    # define how the object will be looked like
    def __str__(self):
        return f"[{self.name}]({self.duration})"

    def __repr__(self):
        return "[{}]({})@{}".format(self.name, self.duration, hex(id(self)))

    def __eq__(self, other):
        print("equal will be performed")
        return super().__eq__(other)

    def __hash__(self):
        #return id(self)
        return hash((self.name, self.duration))

# 先比hash過了才再比 eq
s1 = set()
p1 = Program("BDPY", "35hr")
p2 = Program("BDPY", "35hr")
s1.add(p1)
s1.add(p2)
print(s1)