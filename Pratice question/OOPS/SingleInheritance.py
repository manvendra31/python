# This is the single inheritance in the python

# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, age):
        # call parent constructor
        super().__init__("Dog")
        self.name = name
        self.age = age

    def make_sound(self):
        print("Woof! Woof!")

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")


# create object
dog1 = Dog("Tommy", 5)

# use parent + child methods
dog1.details()        # Child method
dog1.make_sound()     # Overridden method from parent
