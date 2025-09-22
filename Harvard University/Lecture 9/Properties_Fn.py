# Here we can see the another feature of the python is "property" that is a attribute too prevent the messup
# it can decorate the code 

class Student:
    def __init__(self, name, age,house):
        if name not in ["Manvendra", "Anup", "Ankit", "Nitesh"]:
            raise ValueError("Invalid name, must be one of [Manvendra, Anup, Ankit, Nitesh]")       # # we can raise the error if some exceptation error occure
        if age <= 0:
            raise ValueError("Age must be greater than 0")                                             # we can raise the error if some exceptation error occure
        self.name = name
        self.age = age
        self.house=house

    def __str__(self):
        return f"{self.name} from {self.house}"      

# Getter
    @property
    def house(self):
        return self._house

# Setter 
    @house.setter
    def house(self,house):
        if house not in ["Bodwal","Munderwa","Basti"]:
            raise ValueError("Invalid address")
        self._house=house


def main():
    student=get_student()   # We we directly run this code we got the error and show some memory location to overcome 
    #student.house="Welcome to bodwal"
    print(student)

def get_student():
    name = input("What is your name: \n")
    age = int(input("What is your age:\n"))
    house = input("Enter your house details \n")
    return Student(name,age,house)


if __name__ == "__main__":
    main()
