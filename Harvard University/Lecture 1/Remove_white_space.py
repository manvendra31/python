
name=input("What is your name?")
name=name.strip()    #removing the whitespace from the string value
# name=name.capitalize() #captilize user name if we give small letter from the first name
name=name.title()    # Here we can see the ouput every word first  letter will come as the first in Capital letter
print("hello,", name)

del name

# Now we can see the what we have been learned above in the single line

name=input("What is your name?")
#Remove WhiteSpace from the string and captalize the first letter
name=name.strip().title()
print("hello,",name)

del name

# another way same as the above code

name1=input("What is your name? \n").strip().title()
print(name1)

del name1