class MyError(Exception): # 繼承父類別 Exception
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Error value=" + repr(self.value)

# 自定義 Exception

try:
    raise MyError(3 * 3)
except MyError as e:
    print("My exception occured")
    print(e)
    print(e.value)