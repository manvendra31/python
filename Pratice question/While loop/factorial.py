def Factorial(c):
    i = 1
    result = 1
    while i <= c:
        result = result * i   # multiply step by step
        i = i + 1             # increment properly
    print("Factorial =", result)

Factorial(5)
