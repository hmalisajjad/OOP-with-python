class Person:
    """ Person example for oop"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID


person01 = Person("Ali", 30, 12)

print(person01.personID)
print(person01.name)
print(person01.age)
