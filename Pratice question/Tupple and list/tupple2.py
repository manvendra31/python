'''
Exercise 1: Perform Basic Tuple Operations
Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.
Access Elements: Access and print the third element of my_tuple.
Tuple Length: Find and print the length of my_tuple
'''



def tupple_module():
    # Create and return the tuple
    return ('1', '2', '3', '4', '5')

def my_tupple():
    # Call tupple_module() and store the returned tuple
    data = tupple_module()
    
    # Access index 3
    print("Element at index 3:", data[3])
    
    try:
        a = len(data)
        print("Length of tuple:", a)
    except AttributeError:
        print("Show the attribute error")

# Call the function
my_tupple()
