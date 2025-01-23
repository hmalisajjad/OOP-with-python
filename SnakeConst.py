class Snake:
    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName

# objects declaration

python01 = Snake("Python")
anaconda01 = Snake("Anaconda")

# printing the objects values

print(python01.name)
print(anaconda01.name)
