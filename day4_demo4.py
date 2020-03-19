def sumFrom(n):
    if n == 0:
        return 0
    else:
        pass
    return sumFrom(n - 1) + n


if __name__ == '__main__':
    x = int(input("Input a digit:"))
    s = sumFrom(x)
    print("the sum from %d is %d" % (s, x))