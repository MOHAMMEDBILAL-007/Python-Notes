class employee:
    company_name = "amazon"# class variable
    def __init__(self,name):
        self.name = name# instance variable
        self.rais = 0.23# instance variable
    def display(self):
        print(f"name of the employee is {self.name} , {self.rais}")
        print(f"company name {self.company_name}")
emp1 = employee("harry")
emp1.display()# when we call this like below ,there is an argument that is passed but it looks like no argument was given
#employee.display(emp1)# when we call the above this is what actually happens

emp2 = employee("black")
emp2.display()
emp2.rais= 20
emp2.display()   

emp3 = employee("hitler")
emp3.company_name = "facebook"# this doesen't change the the class variable 
# this creates an instance variable that is used insted of the class variable for the instance
emp3.display()
emp4 = employee("nepolian")
emp4.display()