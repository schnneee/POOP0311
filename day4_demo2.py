import math


def square_root(x):
    return math.sqrt(x)


print(square_root(5))
print(square_root(10))

# 就箭頭函式 square_root2(x) => math.sqrt(x);
# 不懂為啥要用冒號
def square_root2(x): return math.sqrt(x)


print(square_root2(4), square_root2(9))

functionVariable1 = lambda x: math.sqrt(x) # var functionVariable1 = (x) => math.sqrt(x);
print(functionVariable1(6), functionVariable1(36))