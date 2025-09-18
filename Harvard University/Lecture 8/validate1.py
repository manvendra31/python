import re

email=input("What is your name?\n").strip()

if re.search(r"^[^@]+@[^@]+\.com$",email):
    print("valid")
else:
    print("Invalid email")  