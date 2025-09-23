# Here we can see the difference between the class and object

class Car:   # PascalCase
    emojis = "🚙🚘🏎️🚓🚔🚗🚋"  # class variable

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def racing(self):
        print(f"{Car.emojis} The car {self.name} (model: {self.model}) is racing!")

# Create object
car1 = Car("Audi", "S7")
car1.racing()



# Now we can create the class and too many object

# here we can see that the object are independent

car2=Car("BMW","NTR")
car3=Car("Tesla","X")

car2.racing()
car3.racing()