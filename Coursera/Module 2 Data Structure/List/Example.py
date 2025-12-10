# we can extract that some spacific word from our txt file by using the split function

a=open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")




for line in a:
    line=line.strip()
    if not line.startswith("From") : continue
    word = line.strip()
    print(word[2])


line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008" 
word=line.split()
print(word)   

