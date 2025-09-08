# Now here we can see writing in the CSV and not overwrite on the same cell each time it write in the down
import csv

name=input("What is your name? \n")
address=input("Where is the address? \n")



#with open(r"D:\python\Harvard University\Lecture 7\Name.csv","a") as file:
#    writer = csv.writer(file)
#    writer.writerow([name,address])
  
# Now we can do with the DictWriter

with open(r"D:\python\Harvard University\Lecture 7\Name.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","address"])
    writer.writerow({"name":name,"address":address})