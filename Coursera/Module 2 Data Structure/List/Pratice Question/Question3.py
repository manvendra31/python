# Find the largest number of the number from the list and  take the input value from the user untill it can't type done

a = []

while True:
    x = input("Enter the number: ")

    if x.lower() == "done":   # makes 'Done' or 'DONE' also work
        break

    try:
        y = float(x)
        a.append(y)
    except:
        print("Invalid input, please enter a number")

print("\nYour list:", a)


# 3️⃣ Method 3 : Using a loop
res = a[0]
for n in a:
    if n > res:
        res = n
print("Largest (loop):", res)


# 1️⃣ Method 1 : Using sort()
a_sorted = sorted(a)     # Use sorted() so original list is not changed
greatest_num = a_sorted[-1]
print("Largest (sort):", greatest_num)


# 2️⃣ Method 2 : Using max()
great_num = max(a)
print("Largest (max):", great_num)
