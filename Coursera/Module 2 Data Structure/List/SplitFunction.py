# we can see the split function

# Example 1: split() with no argument (whitespace)
line = 'A lot    of spaces'
etc = line.split()
print(etc)
print("Length:", len(etc))

print('-' * 40)

# Example 2: split() without matching separator
line = 'first;second;third'
thing = line.split()
print(thing)
print("Length:", len(thing))

print('-' * 40)

# Example 3: split() with separator ';'
thing = line.split(';')
print(thing)
print("Length:", len(thing))
