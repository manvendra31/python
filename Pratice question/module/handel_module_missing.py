# We can handel if module is missing while importing
try:
    import module2
    add(5,6)
except ModuleNotFoundError:
    print("Module is not found")