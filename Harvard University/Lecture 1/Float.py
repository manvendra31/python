x=float(input("What is X?\n"))
y=float(input("What is Y?\n"))
z=x+y
print(z)
# Above is print value in the float form only


# If we want our out in the integer for then we need to convert into integer as show in the below
print(int(z))

del z
#another option is the roundoff python function

z=round(x+y)
print(f"{z:,}")

del z

z=x/y
print(z)
del z

# now we roundoff how many digit after  number i want to see the degit

z=round(x/y,2)
print(z)
del z

# same as the extact output value with different method
z = x/y
print(f"{z:.2f}")