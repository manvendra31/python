# We can formaing
'''
name = input("What is your name?\n").strip()
if "," in name:
    last, first =  name.split(" , ?")
    name = f"{first} {last}"
print(f"Hello, {name}")
'''

import re

name = input("What is your name?\n").strip()
matches = re.search(r"^(.+), (.+)$",name)

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")    


if matches:
    name = matches.group(2)+ " " + matches.group(1)
print(f"hello, {name}")    