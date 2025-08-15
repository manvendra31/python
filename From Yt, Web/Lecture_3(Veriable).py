a = 10
b = "hello how are you"
print(a,b)
# Now we can see dynamic veriable assign like different data in the previous veriale
b = 'i am fine'
print(b)

# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(f)  
print(s2)

print(type(a))
print(type(b))
print(type(s))
print(type(n))
print(type(cnt))
print(type(f))
print(type(age))
print(type(s2))


# Object Reference in the Python
x = 10
y = x
print(y)

# Now we can see use of the del function

'''

del x

y = x
print(y)
# Now we got the error that x is not defined because we have been the delete the variable of the x now we going the assging

'''

# Now we can see the counting the character in the sting

s1 = input("Enter the Sentence: ")
print(s1)
length = len(s1)
print(length)