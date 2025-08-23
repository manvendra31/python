# Print a Right-Angle Triangle with Repeating Numbers

a=int(input("Enter the Number:\n"))
for i in range(1,a+1):
    for j in range(i):
        print(i,end="")
    print()