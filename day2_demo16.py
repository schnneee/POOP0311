import sys

print("process command line arguments")
print(sys.argv)
for arg in sys.argv:
    print(arg)


def func3(**kwargs): # **為dictionary
    print('----')
    for key, value in kwargs.items():
        print("[%s]:%s" % (key, value))
    print('----')


func3()
func3(name='Poop')
func3(name='Poop', duration='35hr')
func3(name='Poop', duration='35hr', location='Taipei', floor='12A')
