# we can see the simple exception handeling
'''
a=10
b=a/0
print(b)
'''
#here in the above code we have seen we got zerodivision error 

a=int(input("Enter the value  of dividend:\n"))
b=int(input("Enter the divisor:\n"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Change the divisor value write other then zero")


