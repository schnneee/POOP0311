class Employee:
    def __init__(self):
        self.work_content = "work"

    def doWork(self):
        print("working on:%s" % self.work_content)


class RD(Employee):
    def __init__(self, work):
        self.work_content = work


class FAE(Employee):
    def __init__(self, work):
        self.work_content = work


class Scientist(Employee):
    def __init__(self, work):
        self.work_content = work


e1 = Employee()
e2 = RD("web front end")
e3 = FAE("hardware integration")
e4 = Scientist("data analyis")

employees = [e1, 35, e2, 3.14, e1, "Hello world", e3, None, e4, e1]
for e in employees:
    if isinstance(e, Employee):
        e.doWork()
    else:
        pass

print(isinstance(e1, Employee), isinstance(e2, Employee), isinstance(e3, Employee), isinstance(e4, Employee))
print(isinstance(e1, RD), isinstance(e2, RD))
print(issubclass(Employee, RD), issubclass(RD, Employee), issubclass(RD, FAE), issubclass(FAE, RD))
print(issubclass(Employee, Employee), issubclass(RD, RD))