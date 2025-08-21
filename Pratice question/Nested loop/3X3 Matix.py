# Now we will print a*a matix by taking the input from the user

a = int(input("Enter the Number you want matix:\n"))
i=j=0
for i in range(a):
    for j in range(a):
        print("*",end="") 
    print()