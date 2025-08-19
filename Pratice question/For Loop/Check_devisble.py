def Divisible(num):
    for i in range(1, 101):   # check first 20 numbers
        if i % num == 0:
            print(f"{i} is divisible by {num}")
        else:
            print(f"{i} is not divisible by {num}")

# take input
x = int(input("Enter a number:\n"))
Divisible(x)
