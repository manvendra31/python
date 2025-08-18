
# This is i want code run untill user give a postive number
'''
while True:
    n=int(input("Enter the number:\n"))
    if n>0:
        break

for _ in range(n):
    print("meow")
'''

# Now we will do same as the use of the function

def main():
    meow(GetNumber())   # call function, not pass function


def GetNumber():
    while True:
        n = int(input("Enter the number:\n"))
        if n > 0:          # properly indented
           break
    return n


def meow(n):
    for _ in range(n):
        print("meow")    


main()
