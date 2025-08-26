# Here we can solve the question regarding the exception on out off index error
def anup():
    n = int(input("How many values you want in the tuple? "))
    temp_list = []

    for i in range(1, n + 1):
        value = input(f"Enter the Value {i} for tuple: ")
        temp_list.append(value)

    return tuple(temp_list)

def manvendra(my_tuple):
    print("Final tuple:", my_tuple)
    search_value = input("Enter the value you want to find the index of: ")
    if search_value in my_tuple:
        print(f"Index of '{search_value}':", my_tuple.index(search_value))
    else:
        print(f"'{search_value}' not found in the tuple.")

def accessing_tuple():
    my_tuple = anup()
    manvendra(my_tuple)

    try:
        a = int(input("Enter the index number you want to access: "))
        print(f"Value at index {a}: {my_tuple[a]}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except IndexError:
        print("You are trying to access an index that is out of range.")

# Run
accessing_tuple()
