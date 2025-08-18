'''

# Now we see how to the print of the list

students = ["Ankit","Manvendra","Nitesh"]
print(students[1])

# Now we can print using the loop

for st in students:      
    print(st)


#Now we can see the len function

for i in range (len(students)):
    print(i+1,students[i]) 

'''

students = {
    "ankit":"Nagendra",
    "manvendra":"Digvijay",
    "Raju":"Nagenndra",
    "Ramu":"Nagendra"
    }

print(students["manvendra"])    
print(students["ankit"])

for st in students:
    print(st)          # we got only just key is printed 


for stu in students:
    print(stu,students[stu],sep=", ")    # here we got both key and value


    