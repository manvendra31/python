# We can handel the exceptation 

try:
    a = int(input("Enter the a: "))

    b = int(input("Enter the b: "))
except ValueError:
    print("only the integer")

try:
    c=a/b
    print(c)
except NameError:
    print("The valueerror")    