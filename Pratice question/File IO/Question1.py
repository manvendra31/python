# To open any text file

f = open(r"D:\python\Pratice question\File IO\Question1.txt", "r")

print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)


# Now we can open the file conntent written

file = open(r"D:\python\Pratice question\File IO\Question1.txt", "r")
content = file.read()
print(content)
file.close()