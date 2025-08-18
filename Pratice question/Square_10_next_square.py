# Now we can see the square from next 10 digit of the user given number

def Square(n):
    for i in range(n+1, n+11):   # i is loop variable, n is function input
        print(i*i)

Square(2)
