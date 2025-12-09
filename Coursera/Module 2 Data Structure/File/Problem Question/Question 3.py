# Print the first 20 characters of a file.

# main.py

from myfile import file

def main():
    f = file()
    content = f.read()
    print(content[:20])
    f.close()

if __name__ == "__main__":
    main()


