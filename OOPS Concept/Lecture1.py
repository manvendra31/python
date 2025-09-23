# Create the class

class DOG:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Dogesh Bhai")
        print(f"Name: {self.name}, Age: {self.age}")


# take inputs
name1 = input("What is the name?\n")
age1 = int(input("Enter the age:\n"))

# create object
dog1 = DOG(name1, age1)

# show details
dog1.details()
