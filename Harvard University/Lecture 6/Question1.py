# Now we can creat the code for the square of the function

def main():
    x=int(input("Enter the number for the square:\n"))
    print("the square of the number",square(x))

def square(n):
    return n*n    


if __name__=="__main__":

    main()