def sum_numbers(start):
    total = 0
    for num in range(start+1, start+101):
        total += num
    print(total)

a = int(input("Enter the first number for the sum of the next 100:\n"))
sum_numbers(a)
