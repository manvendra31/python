# Read the CSV file

students=[]

with open("D:\python\Harvard University\Lecture 7\CSV.csv") as file:
    for line in file:
        name, house=line.rstrip().split(",")
        student={"name":name,"house":house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted (students,key=get_name):
    print(f"{student['name']} is in {student['house']}")       
       
# for sorted in the reverse
for student in sorted (students,key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")  


# For the sorting by house    

def get_house(student):
    return student["house"]

for student in sorted (students,key=get_house):
    print(f"{student['name']} is in {student['house']}")  

# Sorting in reverse order
for student in sorted (students,key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")  
    