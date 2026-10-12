#getters and setters
# old style of getters and setters
class school:
    def __init__(self):
        self._name = None
        self._course = None
        self._uid = None
    def set_details(self,name,course,uid):
        if not name or not course or not uid:
            raise ValueError("name or course or uid cannot be empty")
        self._name=name
        self._course=course
        self._uid = uid
    def get_details(self):
        return f"{self._name}\n{self._course}\n{self._uid}"
student1 = school()
student1.set_details("giga chad","body building","2020BDB066")
print(student1.get_details())


# modern style of using getters and users
class college:
    def __init__(self):
        self._name = None
        self._course = None
        self._uid =None
# must give same name for getter and setter
    @property# this decorator makes the method to appear as a property of the class
    def details(self):# whenever this is called the 'property' decorator already gets the details
        return f"{self._name}\n{self._course}\n{self._uid}"
    
    @details.setter
    def details(self,info):# whenever this is called ".setter" decorator helps to represent this method as a variable
        name,course,uid=info
        if (not name) or (not course) or (not uid):
            raise ValueError("name or course or uid cannot be empty")
        self._name = name
        self._course = course
        self._uid = uid
student2 = college()
student2.details = ("ichigo","soul reaper","1998SLR023")# it appears like iam assigning a property but behind the scean it is a method
print(student2.details)#it looks like iam accessing a property but it is actually a method