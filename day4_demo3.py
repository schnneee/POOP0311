def make_increment(n):
    return lambda x: x + n


print(type(make_increment), type(make_increment(1)))
tenIncrement = make_increment(10) # x = 10
fiveIncrement = make_increment(5) # x = 5
# tenIncrement(1)=> x = 10, n = 1 => 11
print(tenIncrement(1), tenIncrement(2), tenIncrement(3))
print(fiveIncrement(4), fiveIncrement(5), fiveIncrement(6))


def make_tuple(p):
    return lambda x: (x, 'p' * p)


t5 = make_tuple(5)
t10 = make_tuple(10)
print(t5('five tuple'), t10('ten tuple'))

foods = [(4, 'Donut', 0.1), (1, 'Banana', 1.5), (3, 'Apple', 4.0), (2, 'Citron', 2.9)]
print(type(foods), foods)
foods.sort(key=lambda x: x[0])
print(foods)
foods.sort(key=lambda x: x[1])
print(foods)
foods.sort(key=lambda x: x[2])
print(foods)