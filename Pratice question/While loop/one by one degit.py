def Digit(a):
    while a > 0:
        digit = a % 10   # extract last digit
        print(digit)
        a = a // 10      # remove last digit

Digit(1234)
