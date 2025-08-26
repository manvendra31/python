temp_list = []
a = int(input("Enter the number of values you want in the tuple:\n"))
for i in range(1, a + 1):
    value = input(f"Enter value {i}: ")
    temp_list.append(value)

Temp_tuple = tuple(temp_list)
print("Final tuple:", Temp_tuple)
