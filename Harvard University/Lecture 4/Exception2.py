# here we can see the exception in the python
'''
try:
   x=int(input("Enter the x?\n"))
except ValueError:
    print("x is not a integer")   
else:
    print(f"x is {x}")    #here loop is runing again and again don't come out from the loop
'''

'''
while True:
    try:
        x=int(input("Enter the x?\n"))
    except ValueError:
        print("x is not a integer")   
    else:
        break

print(f"x is {x}")       
'''
'''
def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x=int(input("Enter the x?\n"))
        except ValueError:
            print("x is not a integer")   
        else:
           return x 
main()    
'''

def main():
    x=get_int("what is x?")
    print(f"x is {x}")


def get_int(pronpt):
    while True:
        try:
            return int(input(pronpt))
        except ValueError:
            pass  
main()