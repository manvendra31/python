# Here we can  create a module
def add(a,b):
    c= a+b
    print(c)

def sub(a,b):
    z=a-b
    print(z)    

def mul(a,b):
    p=a*b
    print(p)    

def divide(a,b):
    try:
        divide=a/b
        print(divide)
    except ZeroDivisionError:
        print("You cannot divide a number by zero")         