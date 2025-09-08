import re

email=input("What is your name?\n").strip()


if re.search(".*@.*",email):
    print("valid")
else:
    print("Invalid email")    

'''
if re.search(".+@.+",email):
    print("valid")
else:
    print("Invalid email")    
'''
