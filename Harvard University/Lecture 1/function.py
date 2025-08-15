
# find the geometric mean (a*b)/(a+b) this is the formula now we can see by using the function
a=8
b=9
c=(a*b)/(a+b)
print(c)
del a,b,c
# now we can see by function
def CalculateGmean(x ,y):
    mean = (x*y)/(x+y)
    print(mean)

CalculateGmean(10,3)   # now we can call the function and put the value

a = 32
b = 9
CalculateGmean(a,b)
del a , b 

def CompersionNumber(a,b):
    if(a>b):
        print("a is grater number")
    elif(a==b):
        print("Both number is equal")
    else:
        print("Second is the grater number")    

c = int(input("Enter the first Number: \n"))
d = int(input("Enter the Second Number: \n"))       
CompersionNumber(c,d)


# if we want create a function but their logic after some time then we use pass keyword

def IsLessThen(m,n):
    pass                   # Now we don't get the error