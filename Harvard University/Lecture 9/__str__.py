# we will see the exceptation of the "raise" 
'''
class Student:
    def __init__(self, name, age):
        if name not in ["Manvendra", "Anup", "Ankit", "Nitesh"]:
            raise ValueError("Invalid name, must be one of [Manvendra, Anup, Ankit, Nitesh]")       # # we can raise the error if some exceptation error occure
        if age <= 0:
            raise ValueError("Age must be greater than 0")                                             # we can raise the error if some exceptation error occure
        self.name = name
        self.age = age


def main():
    student=get_student()   # We we directly run this code we got the error and show some memory location to overcome 
    print(student)

def get_student():
    name = input("What is your name: \n")
    age = int(input("What is your age:\n"))
    return Student(name, age)


if __name__ == "__main__":
    main()
'''

'''
# To overcome above code error we can rewrite the above code with __str__     
class Student:
    def __init__(self, name, age):
        if name not in ["Manvendra", "Anup", "Ankit", "Nitesh"]:
            raise ValueError("Invalid name, must be one of [Manvendra, Anup, Ankit, Nitesh]")       # # we can raise the error if some exceptation error occure
        if age <= 0:
            raise ValueError("Age must be greater than 0")                                             # we can raise the error if some exceptation error occure
        self.name = name
        self.age = age
    def __str__(self):
        #return "a student"  
        return f"{self.name} from {self.age}"    


def main():
    student=get_student()   # We we directly run this code we got the error and show some memory location to overcome 
    print(student)
  

def get_student():
    name = input("What is your name: \n")
    age = int(input("What is your age:\n"))
    return Student(name, age)


if __name__ == "__main__":
    main()
'''   

# Now we can add more veriable in the our code


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


def main():
    student=get_student()   # We we directly run this code we got the error and show some memory location to overcome 
    print(student)
  

def get_student():
    name = input("What is your name: \n")
    age = int(input("What is your age:\n"))
    id = int(input("Enter your age in the number \n"))
    return Student(name,age,id)


if __name__ == "__main__":
    main()
   