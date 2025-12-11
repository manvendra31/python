# Remove the duplicate from the list 
# Open the file
with open(r"D:\python\Coursera\Module 2 Data Structure\List\romeo.txt") as f:

    unique_words = []

    for line in f:
        words = line.split()
        for w in words:
            if w not in unique_words:
                unique_words.append(w)

print(unique_words)
