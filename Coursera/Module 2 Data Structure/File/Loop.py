nh = open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")

count = 0
for line in nh:
    count += 1
print(count)

nh = open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")  # reopen
re = nh.read()
print(len(re))

