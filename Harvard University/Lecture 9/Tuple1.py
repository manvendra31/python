# Now we can see the same code in the different way
'''
def main():
    student=get_student()
    print(f"{student['Name']} from {student['House']}")

def get_student():
    Name = input("Name:- ")
    House = input("House:- ")
    return {"Name":Name,"House":House}

if  __name__=="__main__":
    main()


'''

def main():
    student = get_student()
    if student["name"] == "Ramu":
        student["house"] = "Jaipur"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name:- ")
    house = input("House:- ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
