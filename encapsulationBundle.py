class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    def employee_details(self):
        print("Employee name is", self.name, "and his salary is ", self.salary)

    def project_work(self):
        print( self.name,"is currently working on", self.project)

# object

emp01 = Employee("Ali", 4000, "Game Development")

# call object with method as public

emp01.employee_details()
emp01.project_work()