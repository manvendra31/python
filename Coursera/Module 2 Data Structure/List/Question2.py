#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
#  When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# Desired Output:-    'Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 
# 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

x = open(r"D:\python\Coursera\Module 2 Data Structure\List\romeo.txt")

unique_words = []

for line in x:
    words = line.split()
    for w in words:
        if w not in unique_words:
            unique_words.append(w)

unique_words.sort()
print(unique_words)
