def func1(x, y, z):
    print('x=', x, ' ,y=', y, ' ,z=', z)


func1('hello', 'world', 'HIHIHI')
func1(1, 5, 3.14)
func1(None, 3, 5)
func1(6, 7, 999)


def func2(*parameters): # 不定長度的參數
    print("_____")
    for p in parameters:
        print('get a parameter:', p)


print("_____")
func2()
func2('hello')
func2('hello', 'world')
func2(3, 4, 5)
func2([3, 4, 5, 6, 7])
func2(*[3, 4, 5, 6, 7]) # 變成一個個進去
func2(*set(list('ABAABABCABCABCCAD'))) # set = distinct 的集合