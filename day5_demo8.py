def getDigit(x):
    returnDigit = 0
    while x > 0:
        x = x // 10
        returnDigit += 1
    return returnDigit


print(getDigit(1024000000))
