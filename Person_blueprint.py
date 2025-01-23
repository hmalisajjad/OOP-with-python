class Person:
    """ Person example for oop"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID


person01 = Person("Ali", 30, 18)
person02 = Person("Umer", 27, 16)
person03 = Person("AbuBakr", 30, 19)

print(person01.personID)
print(person01.name)
print(person01.age)

print(person02.personID)
print(person02.name)
print(person02.age)

print(person03.personID)
print(person03.name)
print(person03.age)