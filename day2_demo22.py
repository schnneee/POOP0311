def addSomething(parameter):
    print("get parameter:", hex(id(parameter)))
    parameter.append('Zebra')
    print("prepare return:", hex(id(parameter)))


animals = ['alpaca', 'baboon']
print('before object passing', hex(id(animals)))
print(animals)
addSomething(animals)
print(animals)
print('after function call', hex(id(animals)))
