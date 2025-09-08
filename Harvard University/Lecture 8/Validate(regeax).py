# Now we can find some pattern

email=input("What is your email?\n").strip()
'''
if "@" and "." in email:
    print("Valid")
else:
    print("Invalid email")    
'''

# Above code have the bugs now we can try another way
username, domain=email.split("@")


if username and domain.endswith(".com"):
    print("valid")
else:
    print("Invalid")
