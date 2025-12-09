# Read a file and print only lines that start with "From ".

def main():
    with open(r"D:\python\Coursera\Module 2 Data Structure\File\mbox-short.txt", "r") as f:
        text = f.read()

    words = text.split()

    if "from" in words:
        index = words.index("from")   # FIRST occurrence
        result = " ".join(words[index + 1:])
        print(result)
    else:
        print("Word not found")

if __name__ == "__main__":
    main()



