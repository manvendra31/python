# We can make the list with the unique text 

fname = r"D:\python\Coursera\Module 2 Data Structure\List\New.txt"

fh = open(fname)

words_list = []

for line in fh:
    words = line.split()
    for word in words:
        if word not in words_list:
            words_list.append(word)

words_list.sort()

print(words_list)