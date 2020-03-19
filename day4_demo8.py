def my_oreo(func):
    def wrapper():
        print("upper side chocolate cookie")
        func()
        print("lower side chocolate cookie")

    return wrapper

@my_oreo # 當作是參數
def add_filling():
    print("butter_cream!")

@my_oreo
def add_peanut_filling():
    print("peanut butter")

@my_oreo
def add_chocolate_filling():
    print("chocolate butter")


fillings = [add_filling, add_peanut_filling, add_filling, add_chocolate_filling]

for fill in fillings:
    print("---")
    fill()
    print("---\n")