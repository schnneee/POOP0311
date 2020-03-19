def my_oreo(func):
    def wrapper():
        print("upper side chocolate cookie")
        func()
        print("lower side chocolate cookie")

    return wrapper


def add_filling():
    print("butter_cream!")


def add_peanut_filling():
    print("peanut butter")


def add_chocolate_filling():
    print("chocolate butter")


fillings = [add_filling, add_peanut_filling, add_filling, add_chocolate_filling]

for fill in fillings:
    print("---")
    get_oreo = my_oreo(fill)
    get_oreo()
    print("---\n")