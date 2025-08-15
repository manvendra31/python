'''
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# Now we see how we take the input from the user

a = input("Please tell me your name: ")
print("hello! ", a , "How are you")
'''

# here we can see how to print the line in the tree different line wwe can use "sep" function
a = "manvendra"
b = 10
c = 10.56

print(a, b, c, sep="\n")


# Now we can take the mulltiple value and then print by using the split function
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)


m , n , o = map(int, input(" enter the three number: ").split())
p = m+n
q = m*o
print(p,q)



######  Find the input DaTaTyPe in the Python
# Above one is the very important topic

d = "hello how are you"
e = 10.5
f = 12
g = ("Geeks", "for", "Geeks")
h = ["Geeks", "for", "Geeks"]
i = {"Geeks": 1, "for":2, "Geeks":3}

print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
