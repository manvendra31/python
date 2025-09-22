# we will see the exceptation of the "raise" 

class Student:
    def __init__(self, name, age):
        if name not in ["Manvendra", "Anup", "Ankit", "Nitesh"]:
            raise ValueError("Invalid name, must be one of [Manvendra, Anup, Ankit, Nitesh]")       # # we can raise the error if some exceptation error occure
        if age <= 0:
            raise ValueError("Age must be greater than 0")                                             # we can raise the error if some exceptation error occure
        self.name = name
        self.age = age


def main():
    try:
        student = get_student()
        print(f"{student.name} is {student.age} years old.")
    except ValueError as e:
        print(f"Error: {e}")


def get_student():
    name = input("What is your name: \n")
    age = int(input("What is your age:\n"))
    return Student(name, age)


if __name__ == "__main__":
    main()