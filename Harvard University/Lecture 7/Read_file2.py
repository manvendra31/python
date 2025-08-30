
# without creating name[] list
'''
with open(r"D:\python\Harvard University\Lecture 7\ABC.txt","r") as file:
    for line in sorted(file):
        print("hello, ",line.rstrip())
  


'''
name=[]

with open(r"D:\python\Harvard University\Lecture 7\ABC.txt","r") as file:
    for line in file:
        name.append(line.rstrip())


for name in sorted(name,reverse=True):  # Sorting in the decending line
    print(f"hello, {name}")        

