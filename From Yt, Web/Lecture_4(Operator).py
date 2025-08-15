# Arithmetic Operators in Python

x = input("Enter a number")
y = input("Enter the second number")

# Typecast to change the value into the int
a=int(x)
b=int(y)

c = a+b   # Addition of the two number
print(c)
c = a-b   #Substraction of the two number
print(c)
c = a*b   # Multiply of the two number
print(c)
c=a/b     # Divide of two number
print(c)
c=a//b    # floor division
print(c)
c=a%b     # Modulas
print(c)
c=a**b    # Exponentation
print(c)

# Compersion Operator

print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a != b)  #Not equal to
del a,b, c

# Logical Oprator

a=True
b=False
print(a and b)
print(a or b)
print(not b)



# Bitwise operatore
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)