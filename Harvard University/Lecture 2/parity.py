x = int(input("Enter the number \n"))
if(x%2==0):
    print("x is the even number")
else:
    print("odd")    

# Now we can do it same by the using the by creating our own function

def parity(a):
    if a%2==0:
        print("the number is the even")  
    else:
        print("The given number is the odd number")      

n=int(input("enter the number for check the parity \n"))
parity(n)        


# Another method that is the most important way by the using if the bollen


def main():
    c = int(input("What is c?\n"))
    if is_even(c):
        print("Even")
    else:
        print("odd")   

def is_even(m):
    if m%2==0:
        return True
    else:
        return False

main()        

