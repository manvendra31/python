# In the below code we can create our own function

class Student:
    def __init__(self, name, age,id):
        if name not in ["Manvendra", "Anup", "Ankit", "Nitesh"]:
            raise ValueError("Invalid name, must be one of [Manvendra, Anup, Ankit, Nitesh]")       # # we can raise the error if some exceptation error occure
        if age <= 0:
            raise ValueError("Age must be greater than 0")                                             # we can raise the error if some exceptation error occure
        self.name = name
        self.age = age
        self.id=id
    def __str__(self):
        #return "a student"  
        return f"{self.name} age is {self.age} and their id is {self.id}"   
    def charm(self):     # here we can create our own function
        match self.age:
            case age if  0 <= age <= 22:
                return "😂😂😂😂😂"
            case age if 23 <= age <= 55:
                return "👯‍♀️👯‍♀️👯‍♀️👯‍♀️👯‍♀️"
            case age if 55<= age <=100:
                return "💀💀💀💀💀"
            case _:
                return "/ dogesh bhai"                 


def main():
    student=get_student()   # We we directly run this code we got the error and show some memory location to overcome 
    print("Expecto Patroum")
    print(student.charm())
  

def get_student():
    name = input("What is your name: \n")
    age = int(input("What is your age:\n"))
    id = int(input("Enter your age in the number \n"))
    return Student(name,age,id)


if __name__ == "__main__":
    main()