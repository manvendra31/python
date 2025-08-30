name = []

with open(r"D:\python\Harvard University\Lecture 7\ABC.txt","r") as file:
    for line in file:
        name.append(line.rstrip())


for name in sorted(name):
    print(f"hello, {name}")        


    