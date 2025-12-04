# Use the file name mbox-short.txt as the file name
fh = open(r"D:\python\Coursera\Module 2 Data Structure\File\mob.txt")
nh = open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")
for x in fh:
    print(x)


# Counting the line in the file

count = 0
for line in nh:
    count = count+1
print(count)    
