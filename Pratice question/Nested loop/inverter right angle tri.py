#print the inverted right angle triangle
a = int(input("Enter the number up to which you want the table:\n"))
i=j=0
for i in range(a,0,-1):
    for j in range(i):
        print("*",end="")
    print()    