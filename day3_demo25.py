def outer(number1):
    def inner_increment(num1): # func內可再放func
        return num1 + 1

    num2 = inner_increment(number1)
    return (num2)


print(outer(10))
print(outer(15))


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sorry, number must be integer")
    if not number >= 0:
        raise ValueError("Sorry, number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)
print(factorial(9))