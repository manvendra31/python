# Now we can see how to create the dictionary

a={1:"Manvendra",2:"Pratap",3:"Singh"}

print(a)


# Now we can see how to create the dictionary

b=dict(x="Manvendra",y="Pratap",z="Singh")
print(b)

print(b["y"])
print(b.get("x"))


# Adding and updating the dictionry

b["Age"]=23
print(b)

b["x"]="Shubham"

print(b)