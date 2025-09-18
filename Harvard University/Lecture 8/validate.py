import re

email=input("What is your email?\n").strip()
'''

if re.search(".*@.*",email):
    print("valid")
else:
    print("Invalid email")    

'''

'''
if re.search(r".+@.+\.com$",email):
    print("valid")
else:
    print("Invalid email")    

'''
# In this code the problem is if user start with @ then it say valid
if re.search(r"[^@]+@[^@]+\.com$",email): # it meaan only one @ will be there and befor and after @ no @ will be there 
    print("valid")
else:
    print("Invalid email")   

# For overcome the upper code we can rewite [A-Z]

if re.search(r"^[A-Za-z0-9][^@]+@[^@]+\.com$",email): # it meaan only one @ will be there and befor and after @ no @ will be there 
    print("valid")
else:
    print("Invalid email")   

# for more  good code 
if re.search(r"^[A-Za-z0-9_ ][^@]+@[^@]+\.com$",email): # it meaan only one @ will be there and befor and after @ no @ will be there 
    print("valid")
else:
    print("Invalid email")  

# if the user the write their email in the captial letter then it show the error

    