# We can ittrate the dictionary

a = dict(x="Manvendra", y="Pratap", z="Singh")

print(a)

# Print keys
for key in a:
    print(key)

# Print values view
print(a.values())

# Print values one by one
for value in a.values():
    print(value)

# Print key-value pairs
for key, value in a.items():
    print(f"{key}: {value}")
