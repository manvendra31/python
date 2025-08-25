import cowsay
import sys

try:
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])  # Corrected to sys.argv[1]
    else:
        print("Usage: python script.py <your_name>")
except IndexError:
    print("Please provide your name as a command-line argument.")
