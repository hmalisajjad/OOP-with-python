class Bird:
    def intro(self):
        print("there are many type of birds")

    def flight(self):
        print("but some can't fly")

class sparrow(Bird):
    def flight(self):
        print("sparrow can fly")

class ostrich(Bird):
    def flight(self):
        print("but ostrich can't fly")

bird1 = Bird()
sparrow1 = sparrow()
ostrich1 = ostrich()

bird1.intro()
bird1.flight()

sparrow1.intro()
sparrow1.flight()

ostrich1.intro()
ostrich1.flight()