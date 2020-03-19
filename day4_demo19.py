from collections import UserList


class MyOwnList(UserList):
    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            self.data[key] = value
            pass
        pass

    def square(self):
        for i in range(0, len(self.data)):
            self.data[i] = self.data[i] ** 2


list1 = MyOwnList()
# list1 = []
for item in range(10):
    list1[item] = 2 * item

print(list1)
list1.square()
print(list1)