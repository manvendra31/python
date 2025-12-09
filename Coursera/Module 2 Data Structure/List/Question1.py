# Average the number but the number will be taken by the user until user type done

total=0
count=0

while True:
    inp = input("Enter the number: \n")
    if inp=="done": break 
    value = float(inp)
    total=total+value
    count=count+1

average = total/count
print(average)    


