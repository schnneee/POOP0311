class Employee:
    def __init__(self):
        self.work_content = "work"

    def doWork(self):
        print("working on:%s" % self.work_content)


class RD(Employee):
    def __init__(self, work): # 複寫父類別的 work_content
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
    if isinstance(e, Employee): # 確認是Employee
        e.doWork()
    else:
        pass