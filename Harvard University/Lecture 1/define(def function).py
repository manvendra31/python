'''
name = input("What is your name? ")
hello()    # this throw the error now we define as the function
print(name)
'''

'''
def hello():     # now here we can define a function as hello is print output hello in the output
    print("hello")




name = input("What is your name? ")
hello()   
print(name)
'''

# In the above question we have been seen that we need to used the print function again and again so we can customize the def function

def hello(to):     # now here we can define a function as hello is print output hello in the output
    print("hello, ",to)

name = input("What is your name? ")
hello(name)
