# Now we can see the public class 

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # public
        self.model = model  # public

car1 = Car("Toyota", "Corolla")
print(car1.brand)  # Accessible
print(car1.model)
