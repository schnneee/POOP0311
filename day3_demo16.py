n = 200
summation = 0
counter = 1
limitation = 2000
while counter <= n:
    summation += counter
    counter += 1
    if summation > limitation:
        break
else:
    print("calculate terminated")

print("sum of 1 till %d ==> %d" % (n, summation))