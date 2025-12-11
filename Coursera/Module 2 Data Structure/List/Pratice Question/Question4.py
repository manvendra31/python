# Find the smallest number in a list (without using min())

# we  can take the input from the user

a=[]

while True:
    x=input("Enter the number:- ")
    if x.lower()=="done":
        break
    b=int(x)
    a.append(b)

print(a)    

# by  using the loop method

res=a[0]

for i in a:
    if res>i:
        res=i
print(res)        


# By usnig the sort function
a.sort()
print(a[0])


# By using the min function

m=min(a)
print(m)
