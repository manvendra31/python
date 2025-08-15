'''
x = int(input("enter the value of the X\n"))
y = int(input("enter the value of the Y\n"))
z = x+y
print("the sum of the two number is: ",z)
'''

# Now we will try from the function
def main():
    x = int(input("Enter the value of X: "))
    y = int(input("Enter the value of Y: "))
    result = add_numbers(x, y)
    print("Sum is:", result)

def add_numbers(a, b):
    return a + b

main()
