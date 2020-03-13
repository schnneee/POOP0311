def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("divide by zero!")
    except Exception as e:
        print("exception!", e)
    else:
        print("result is", result)
    finally:
        print("execution closed")

divide(2, 1)
divide(2, 0)
divide("2","0")