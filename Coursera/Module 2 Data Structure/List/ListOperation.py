# We can perform many operation in the list

a=[10,5,45,85]
b=[65,94,5,5,778]

c=a+b

print(c)

d=c*3
print(d)


print(d[2:5])
print(d[:5])
print(d[2:])


# we can add data in the list

a.append(5535)

print(a)


# Deleting the element

f=a.pop(3)

print(f)

print(a)    # Now update the list after removing the 3rd index value

del a[1]

a.remove(10)

print(a)