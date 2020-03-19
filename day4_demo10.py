def my_oreo(func):
    def wrapper(*x):
        print("[-----------]")
        print("upper side chocolate cookie")
        func(*x)
        print("lower side chocolate cookie")
        print("[===========]")
    return wrapper


@my_oreo
def add_filling(*fills): # pointer

    for fill in fills:
        print("%s_cream!" % fill)


add_filling()
add_filling('cherry')
add_filling('cherry', 'pineapple', 'mint_chocolate')