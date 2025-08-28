# We can see the list I/O

'''
names=[]
for _ in range(3):
    names.append(input("What is name? \n"))

for name in sorted(names):
    print(f"Hello, {name}")

'''

name=input("What is your name?\n")

file=open("name.txt","a")

file.write(name)

file.close()