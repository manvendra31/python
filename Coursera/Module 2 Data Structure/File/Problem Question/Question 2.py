# Count the number of lines in mbox-short.txt.

ram = open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")

#a = ram.read()   # reads the whole file

#ram.seek(0)      # reset pointer to beginning

count = 0
for line in ram:
    count += 1

print("Number of lines:", count)

'''
# Here in the both print statement we can count the number of the character 
count = 0 

for i in a:
    count = count+1
print(count)

print(len(a))

'''