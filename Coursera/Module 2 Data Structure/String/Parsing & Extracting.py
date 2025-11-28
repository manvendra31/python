data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print (atpos)
sppos = data.find(' ',atpos)
print (sppos)
host = data[atpos+1 : sppos]
print (host)



data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


for letter in 'banana' :
    print(letter)



x = 'From marquard@uct.ac.za'

print(x[14:17])

x = '40'
y = int(x) + 2
print(y)