def CountDigit(n):
    count = 0
    while n > 0:
        count = count + 1      # increase digit count
        n = n // 10            # remove last digit
    print("The number of digits in the number are:", count)

a = int(input("Enter the number: \n"))
CountDigit(a)
