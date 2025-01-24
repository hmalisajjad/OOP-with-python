class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private attribute declaration

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

per1 = Person("Ali", 34)

# modify private age

per1.set_age(35)

print(" Person name is", per1.name, "His age is", per1.get_age() )