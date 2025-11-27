hrs = input("Enter Hours:")
h = float(hrs)
rate1=input("Enter Rate:")
r1=float(rate1)
rate2=input("Enter Rate:")
r2=float(rate2)


if h>40.00:
    a=h-40
    c=a*r2
    d=40*r1
    print(c+d)
else:
    a=h*r1
    print(a)