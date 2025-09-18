# As we have seen the previous file validate.py file that if the user write their email in the captital letter then it throw the error

import re

email=input("What is your email?\n").strip()

# to ignore the capital letter error

if re.search(r"^[a-z0-9_ ][^@]+@[^@][a-z]+\.com$",email,re.IGNORECASE): 
    print("valid")
else:
    print("Invalid email")  


#Above code have too many arrguments so we can rewrite the code by the differnet way

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

