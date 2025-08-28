# We can see how user give the input and output give as per their input using Pytest 

def squ():
    print("The square of the number is", inp())

def inp():
    a = int(input("Enter the value of a: "))  
    return a + a  

def main():
    squ()


if __name__=="__main__":
    main()
