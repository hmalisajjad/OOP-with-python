# parent class

class Vehicle:
    def Vehicle_data(self):
        print("parent vehicle class")

# child class

class Car(Vehicle):
    def Car_data(self):
        print("child Car class")


#object with method call
car01 = Car()

# get vehicle data
car01.Vehicle_data()
car01.Car_data()