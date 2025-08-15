
'''
def hello(to="world"):
    print("hello,",to)

hello()
name = input("What is your name? ")
hello(name)    
'''

'''
# now we see we define our function in the last part not as the first
def main():
    name = input("What is your name? ")
    hello()

def hello():
    print("hello,",name)
main()

'''



# Now we can see another example for the square of a nummber

def main():
    x=int(input("please give a number\n"))
    print("the square of your given number is ", square(x))

def square(n):
    return n*n

main()