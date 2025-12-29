# How we ccan sorted by the value
# 
# 

a = {'A':58,'C':2,'B':52}
temp = list()

for k,v in a.items():
    temp.append((k,v))

print(temp)    


temp=sorted(temp,reverse=True)
print(temp)


x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

print(y)