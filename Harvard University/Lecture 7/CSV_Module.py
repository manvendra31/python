# Now we can see how to how to import the csv file from the module
'''
import csv

Stock=[]

with open(r"D:\python\Harvard University\Lecture 7\AAPL.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        Stock.append({"Date":row[0],"High":row[2]})

for ShareMarket in sorted(Stock,key=lambda ShareMarket:ShareMarket["Date"]):
    print(f"{ShareMarket['Date']} is {ShareMarket['High']}")
'''

# Insted of CSV reader we used DictReader(This is used maybe someone changed change the excel the abouve code take as the  )

import csv

Stock=[]

with open(r"D:\python\Harvard University\Lecture 7\AAPL.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        Stock.append({"Date":row["Date"],"High":row["High"]})

for ShareMarket in sorted(Stock,key=lambda ShareMarket:ShareMarket["Date"]):
    print(f"{ShareMarket['Date']} is {ShareMarket['High']}")