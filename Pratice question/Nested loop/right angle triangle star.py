#print the right angle triangle

i=j=0
a = int(input("Enter the number up to which you want the table:\n"))
for i in range(a+1):
    for j in range(i):
        print("*",end="")
    print()    