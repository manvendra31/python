# We can see how we can split the list 

m="Manvendra;Pratap;Singh;Bodwal;Basti"
print(m)

z=m.split(";")

print(len(z))

print(z)

# In we can split the above one string into the list by using the split function

# What if we have lots of the space in the given

a = "Ankit,Singh        ,                   Bodwal,Basti"

z = [item.strip() for item in a.split(",")]
print(z)
