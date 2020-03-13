class Program:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    # define how the object will be looked like 看起來長怎樣(print出來的格式)
    def __str__(self):
        return f"[{self.name}]({self.duration})"

    def __repr__(self): # 轉換 print 出來的格式，可查看所指對象
        return "[{}]({})@{}".format(self.name, self.duration, hex(id(self)))

    def __eq__(self, other): # 如何相等
        return self.name == other.name and self.duration == other.duration

    def __hash__(self):
        # 只有 imutable可做hash
        # return id(hash) 沒屁小用，因為大家記憶體位置不同
        # return hash(self.name + self.duration) 可以但不佳
        return hash((self.name, self.duration)) # 建議使用
        #return hash([self.name, self.duration]) 不可使用，因為list 為 mutable

# eq和hash都相等才算相等

p1 = Program("POOP", "35hr")
print('hash for p1=', hex(hash(p1)))
print(p1)
p2 = Program("POOP", "35hr")
print('hash for p2=', hex(hash(p2)))
print(p2)
p3 = Program("BDPY", "35hr")
print('hash for p3=', hex(hash(p3)))
print(p3)
p4 = p1
print(p4)

s1 = set()
s1.add(p1)
print(s1)
s1.add(p2)
print(s1)
s1.add(p3)
print(s1)
s1.add(p4)
print(s1)