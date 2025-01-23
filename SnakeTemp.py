class Snake:
    """Snake main blueprint"""
    name = "Python"

    # method to change name
    def modifyName(self, new_name):
        self.name = new_name

#Objects based on Snake

snake01 = Snake()

# printing on screen
print(snake01.name)

# modify the name using constructor method modifyName
snake01.modifyName("Anaconda")
print(snake01.name)