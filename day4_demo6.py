def infinite_generator(start=0):
    while True:
        yield start #不會建立一個新的 call stack
        start += 2


p = infinite_generator(5)
# print(next(p),next(p),next(p))

for n in infinite_generator(5):
    print(n)
    if n > 50:
        break