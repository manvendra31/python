# Here we can see the method inside the class

class Car:   # PascalCase
    emojis = "🚙🚘🏎️🚓🚔🚗🚋"  # class variable

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def racing(self):
        print(f"{Car.emojis} The car {self.name} (model: {self.model}) is racing!")

    def remodeling(self,new_model):
        self.model=new_model
        print(f"the model of the car have been changes to {new_model}")

# Create object
car1 = Car("Audi", "S7")
car1.racing()
car1.remodeling("Tesla")
car1.racing()
