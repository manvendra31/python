# Print the sum of first N even numbers.
N = int(input("Enter how many even numbers sum you want: "))

total = 0
for i in range(1, N + 1):   # loop from 1 to N
    even_number = 2 * i     # generate the ith even number
    total += even_number    # add to sum

print("Sum of first", N, "even numbers is:", total)


