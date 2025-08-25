# Now we can find the index of the following by the user

# Step 1: Ask how many values the user wants
n = int(input("How many values do you want to store in the tuple? "))

# Step 2: Take that many values from the user
temp_list = []
for i in range(n):
    value = input(f"Enter value {i+1}: ")
    temp_list.append(value)

# Convert the list to a tuple
b = tuple(temp_list)
print("\nYour tuple is:", b)

# Step 3: Allow the user to access index values repeatedly
while True:
    a = input("\nEnter the index you want to access (0–{}), or 'q' to quit: ".format(n-1))

    if a.lower() == 'q':
        print("Exiting...")
        break

    try:
        index = int(a)
        print("Value at index", index, "is:", b[index])
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid index (0–{}) or 'q'.".format(n-1))
