# Remove extra spaces from each line and print clean output

a = open(r"D:\python\Coursera\Module 2 Data Structure\File\python_variations.txt")

for line in a:
    clean = " ".join(line.split())   # remove extra spaces but keep line
    print(clean)

a.close()
