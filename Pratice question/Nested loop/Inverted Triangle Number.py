# Here we can print the number in the right angle

a = int(input("Enter the number:\n"))

for i in range(a, 0, -1):        # Start from a down to 1
    for j in range(1, i+1):      # Start from 1 to i
        print(j, end=" ")
    print()                      # New line after each row
