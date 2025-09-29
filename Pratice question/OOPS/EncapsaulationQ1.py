# Here we can see about the encapsulation and it's feature

class Employee:
    a = "This is the employee class"

    def __init__(self, salary, name):
        self.__salary = salary   # private variable
        self.name = name

    def show_salary(self):
        print(self.__salary)     # access private variable inside class


emp = Employee(56000, "Manvendra") 
print(emp.name)          # prints "Manvendra"
emp.show_salary()        # prints 56000
# print(emp.__salary)    # ❌ Error: can't access private attribute



# access to __salary, you can also use getter and setter method

class Employee:
    def __init__(self, salary, name):
        self.__salary = salary
        self.name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")


emp = Employee(56000, "Manvendra")
print(emp.get_salary())   # ✅ 56000
emp.set_salary(65000)
print(emp.get_salary())   # ✅ 65000
