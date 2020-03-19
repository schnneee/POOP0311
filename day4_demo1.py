def outer():
    x = "local"
    print("[1]x=", x)

    def inner():
        nonlocal x #巢狀函數內宣告外部變數，使巢狀函數能夠使用外層函數的區域變數
        x = "local under inner"
        print("[2]x=", x)

    print("[3]x=", x)
    inner()
    print("[4]x=", x)

outer()