# 物件也可以迭代
class Counter(object):
    def __init__(self, low, high):
        print("object construct")
        self.current = low
        self.high = high
        pass

    def __iter__(self): # 迭代時返回
        print("object start to iterate")
        return self

    def __next__(self): # 做啥，啥時停止
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
        # raise StopIteration


c1 = Counter(5, 15)
for c in c1:
    print(c)

c2 = Counter(5, 10)
print([c for c in c2])

s1 = "hello world"
for s in s1:
    print(s)