import numpy
a1 = ['apple', 'banana']
a2 = ['orange', 'kiwi']
print(a1 + a2)
b1 = [1, 2, 3]
b2 = [4, 5, 6]
print(b1 + b2)
# 一般陣列香家為長度相加，使用 numpy.array 可讓陣列元素相加
c1 = numpy.array([1, 2, 3])
c2 = numpy.array([4, 5, 6])
print(c1 + c2)
print("for demo2 itself", __name__)
print("for numpy,", numpy.__name__)