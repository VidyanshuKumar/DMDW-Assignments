class Employee:
    def __init__(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.basic = float(input("Enter Basic Pay: "))

    def calc(self):
        self.ta = self.basic * 10 / 100
        self.da = self.basic * 40 / 100
        self.gross = self.basic + self.ta + self.da

    def disp(self):
        print("\nEmployee ID :", self.empid)
        print("Name :", self.name)
        print("Basic Pay :", self.basic)
        print("TA :", self.ta)
        print("DA :", self.da)
        print("Gross Pay :", self.gross)


e = Employee()
e.calc()
e.disp()