# Now here we can also add the object with the class

class dog:
    species =  "BullDog"

    def __init__(self):
        self.name=input("Enter the name of Dog: \n")
        self.age=int(input("Enter the age of dog: \n"))

dog1 = dog()

print("Dog's Name:", dog1.name)
print("Dog's Species:", dog1.species)
print("Dog's Age:", dog1.age)


dog2=dog()
print("Dog's Name:", dog2.name)
print("Dog's Species:", dog2.species)
print("Dog's Age:", dog2.age)



# second method to print more then 2 data enter and print

class Dog:
    species = "BullDog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# create two dogs by passing values
dog1 = Dog("Bruno", 5)
dog2 = Dog("Tommy", 3)

print("\nDog 1:", dog1.name, dog1.age, dog1.species)
print("Dog 2:", dog2.name, dog2.age, dog2.species)
