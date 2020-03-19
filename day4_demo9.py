def my_oreo(func):
    def wrapper(x):
        print("upper side chocolate cookie")
        func(x)
        print("lower side chocolate cookie")

    return wrapper


@my_oreo
def add_filling(fill):
    print("%s_cream!" % (fill))


add_filling('vanilla_chocolate')

# get_oreo = my_oreo(add_filling)
#
# get_oreo()