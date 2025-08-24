# we can handel 2 exceptation
try:
    a=int(input("Enter the value  of dividend:\n"))
    b=int(input("Enter the divisor:\n"))
    c=a/b
except ZeroDivisionError:
    print("Change the divisor value write other then zero")
except ValueError:
    print("Enter the integer value")  
else:
    print("Result is", c)
    
finally:
    print("Execution complete.")      

