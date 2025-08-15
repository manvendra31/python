value = input("Enter something: ")

# Always string from input()
print("Raw type from input():", type(value))

# Check if it represents an integer
if value.isdigit():
    print("It can be converted to an integer.")
    value = int(value)
    print("Converted type:", type(value))

# Check if it represents a float
elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
    print("It can be converted to a float.")
    value = float(value)
    print("Converted type:", type(value))

# Otherwise it's a string
else:
    print("It is a string.")
