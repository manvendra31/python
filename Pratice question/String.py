'''
a = "good afternoon"
b = input("What is your name?\n")
print(f"{a}!\n{b}")
'''
# Write the letter as per the given templet

'''
a=input("Enter the name ")
b=input("Enter the date")
c="you are selected !"
print("Dear "+a,"\n"+c+"\n"+b)

'''


# Write a program to detect the double space in string (most important concept)
'''
a=input("Enter the string")
if "  " in a:
    print("Double space found in the string")
else:
    print("string doesn't have the double space")    
'''

# Now we can remove the double space with the single space

a=input("Enter the string and in between give double space \n")

if "  " in a:
    print("String have the double string")
    while "  "in a:
        a=a.replace("  "," ")
        print("The fixed string is: \n",a)
else:
    print("Your String does't have the double string")        