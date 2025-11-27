def computepay(h, r):
    if h > 40:
        overtime = h - 40
        overtime_pay = overtime * (1.5 * r)
        normal_pay = 40 * r
        total = normal_pay + overtime_pay
        return total
    else:
        pay = h * r
        return pay    

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
p = computepay(hrs, rate)
print("Pay:", p)
