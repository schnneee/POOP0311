class Employee:
    company = "uuu"

    def __init__(self):
        print("init method is called")
        pass

    def working(self):
        self.working_hour = 7
        return self.working_hour * 5

    def dailyWorkingHour(self):
        return self.working_hour

    pass


e1 = Employee()
e2 = Employee()
print(e1.company, e2.company, Employee.company)
Employee.company = "systex"
print(e1.company, e2.company, Employee.company)
e1.company = "oracle"
print(e1.company, e2.company, Employee.company)
print("e1 weekly working hour:", e1.working())
print("e1 daily working hour:", e1.dailyWorkingHour())