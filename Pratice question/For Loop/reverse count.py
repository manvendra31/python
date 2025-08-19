def ReverseCount(a, b):
    if a > b:   # only works if first number is bigger
        for i in range(a, b-1, -1):
            print(i)
    else:
        print("First number must be greater than the second number!")

# take input
x = int(input("Enter the number of X:\n"))
y = int(input("Enter the number of Y:\n"))

ReverseCount(x, y)   # use lowercase x, y
