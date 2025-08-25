import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])  # Displays the cow with your message
else:
    print("Usage: python script.py <your_name>")
