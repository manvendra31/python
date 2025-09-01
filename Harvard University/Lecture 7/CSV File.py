# Read the CSV file

with open("D:\python\Harvard University\Lecture 7\CSV.csv") as file:
    for line in file:
        name, house=line.rstrip().split(",")
        print(f"{name} is in {house}")
