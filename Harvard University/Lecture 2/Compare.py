x = int(input("What is x?"))

y = int(input("What is y?"))


if x<y:
    jls_extract_var = "x is the less the y"
    print(jls_extract_var)

elif x>y:

    print("x is grater then y") 

else:

    print("x is equal to y")       

del x,y

# Now we can approch them by the differemt way putting OR function

x = int(input("What is x?"))

y = int(input("What is y?"))


if x<y or x>y:    # here we can use OR operator

    print("x is not equal to y")

else:

    print("x is equal to y")    