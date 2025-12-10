# We can see how to do that the double split



line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008" 

word=line.split()
print(word[1])
z=word[1]

pieces = z.split('@')

print(pieces)



friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])



t = [9, 41, 12, 3, 74, 15]

print(t[2:4])



x = list(range(5))
print(type(x))




fruit = 'Banana'
fruit[0] = 'b'
print(fruit)