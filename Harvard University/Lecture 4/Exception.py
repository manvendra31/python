# here we can see the exception in the python
try:
   x=int(input("Enter the x?\n"))
   print(f"x is {x}")
except ValueError:
    print("x is not a integer")   