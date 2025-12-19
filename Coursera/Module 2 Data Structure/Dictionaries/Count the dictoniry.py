# We can count the number of word appear in the in the dictonry by a file

a = open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt")

b = a.read()

word_count = dict()

words = b.split()   # split text into words

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


