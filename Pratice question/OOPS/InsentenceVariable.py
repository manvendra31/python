# Now we can see the Insentence Variable

class Car:
    wheels = 4   # class variable (common for all cars)

    def __init__(self, brand, color):
        self.brand = brand   # instance variable
        self.color = color   # instance variable

car1 = Car("BMW", "Red")
car2 = Car("Tesla", "Black")

print(car1.wheels)  # 4
print(car2.wheels)  # 4

Car.wheels = 6      # update class variable
print(car1.wheels)  # 6
print(car2.wheels)  # 6
