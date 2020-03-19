class Employee:
    def __init__(self):
        self.work_content = "work"

    def doWork(self):
        print("working on:%s" % self.work_content)


class RD(Employee): # 繼承Employee
    pass


class FAE(Employee):
    pass


class Scientist(Employee):
    pass
e1 = Employee()
e2 = RD()
e3 = FAE()
e4 = Scientist()

e1.doWork()
e2.doWork()
e3.doWork()
e4.doWork()