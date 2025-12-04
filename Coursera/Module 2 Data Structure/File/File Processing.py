# We can read the file

fhand = open(r"D:\python\Coursera\Module 2 Data Structure\File\mob.txt")
# print(fhand.read())


for i in fhand:
    print(i)


count = 0

for line in fhand:
    count = count+1
print("Line count: ", count)    
