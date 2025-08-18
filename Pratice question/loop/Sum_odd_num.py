# Sum of the fisrt n odd number

N = int(input("Enter how many odd numbers you want the sum of: "))

total = 0
for i in range(1, 2*N, 2):   # generates odd numbers: 1,3,5...
    total += i

print("Sum of first", N, "odd numbers is:", total)
