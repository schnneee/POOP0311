numbers = [5, 3, 11, 29, 4, 6, 7, 10, 8, 3, 99, 240]

sum = 0

for n in numbers:
    sum += n

print("sum=%d" % sum)

numbers = [5, -3, 11, -29, 4, -6, 7, -10, 8, -3, 99, -240]

for n in numbers[:]:
    if (n < 0):
        numbers.remove(n)
        pass
    pass
print(numbers)
numbers = [5, -3, 11, -29, 4, -6, 7, -10, 8, -3, 99, -240]
print("start ro run 3rd loop")
for n in numbers[:]: #=> 加[:] 在跑回圈時先建立複本
    if (n < 0):
        numbers.insert(0, n)
        #print(numbers)
print(numbers)