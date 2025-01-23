class Person:
    """ Person example for oop"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

    def display_data(self):
        print("Hi my name is", self.name, ". I am", self.age, "years old and my ID is", self.personID)


person01 = Person("Ali", 30, 18)
person02 = Person("Umer", 27, 16)
person03 = Person("AbuBakr", 25, 19)

person01.display_data()
person02.display_data()
person03.display_data()