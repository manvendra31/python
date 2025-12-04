# We can read the file and then we can print the file in the upper case

a = open(r"D:\python\Coursera\Module 2 Data Structure\File\word.txt")

b = a.read()

print(b)

c = (b.upper())

print(c)


print(c.strip())
