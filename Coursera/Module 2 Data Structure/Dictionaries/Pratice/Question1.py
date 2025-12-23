# Create a disctionary from the list and count the how many number of the fruit

lst = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for fruit in lst:
    count[fruit] = count.get(fruit, 0) + 1

print(count)
