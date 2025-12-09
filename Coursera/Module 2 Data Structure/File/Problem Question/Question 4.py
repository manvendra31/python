# Count how many times the word “python” appears in a file (case-insensitive)

a = open(r"D:\python\Coursera\Module 2 Data Structure\File\python_variations.txt")

b = a.read()

print(b)

c = b.upper()

print(c)

a.seek(0)

count =c.count('PYTHON')

print(count)