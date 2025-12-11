# Print all even numbers from a list

#Here is the list
nums = [10, 25, 32, 41, 50]
new_list=[]

for i in nums:
    if i%2==0:
        new_list.append(i)

print(new_list)
