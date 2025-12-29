# We can sorted the tuple

a = {'A':58,'C':2,'B':52}

b=sorted(a.items())

print(b)

for k ,v in sorted(a.items()):
    print(k,v)


# How we ccan sorted by the value
# 
# 

temp = list()

for k,v in a.items():
    temp.append(k,v)

print(temp)    