class Employee:
    company = "samsung"
    def details(self):
        print("welcome")
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


e1 = Employee()
e1.details()
print(Employee.company)

e1.change_company("google")
print(Employee.company)# class wariable changed
