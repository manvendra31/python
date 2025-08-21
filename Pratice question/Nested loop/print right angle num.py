# Here we can print the number in the right angle

a=int(input("Enter the number:\n"))
i=j=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    