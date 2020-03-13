data = [[1, 2, 3, -4, 5],
        [6, 7, 8, 9, 10],
        [1, 3, 5, 7, 9],
        [2, 4, -6, 8, 10]]
print("break usage:")
for row in data:
    sum = 0
    for col in row:
        if col < 0:
            print("got an outlier %d" % col)
            break
        else:
            sum += col
    else:
        print('row sum = %d' % sum)
print("====column usage:=====")
for row in data:
    sum = 0
    for col in row:
        if col < 0:
            print('got an outlier %d' % col)
            continue
        else:
            sum += col
    else:
        print('row sum=%d' % sum)


