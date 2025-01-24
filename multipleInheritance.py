class Person:
    def person_data(self, name, age):
        print("Employee name is ", name, ", his age is ", age)
    
class Company:
    def company_data(self, comp_name, location):
        print("Our Company name is", comp_name, "and we are located in", location)

# child class

class Employee(Person, Company):
    def employee_data(self, salary, skills):
        print("Salary is", salary, "his skills are", skills)

#objects with method

emp01 = Employee()

emp01.person_data("Ali", 35)
emp01.company_data("ABCD", "Berlin")
emp01.employee_data(50000, "Software Developer")